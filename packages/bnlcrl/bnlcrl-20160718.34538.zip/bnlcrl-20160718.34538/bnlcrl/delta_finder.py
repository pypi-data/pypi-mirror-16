#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Get delta (index of refraction).

Several methods are supported:
- get delta from http://henke.lbl.gov/optical_constants/getdb2.html;
- calculate delta analytically.

Author: Maksim Rakitin (BNL)
2016
"""

import math
import os

from bnlcrl.utils import convert_types, defaults_file, read_json

DEFAULTS_FILE = defaults_file(suffix='delta')['defaults_file']


class DeltaFinder:
    def __init__(self, **kwargs):
        # Check importable libs:
        self._check_imports()

        # Get input variables:
        d = read_json(DEFAULTS_FILE)

        self.defaults = d['defaults']
        self.parameters = convert_types(d['parameters'])

        self.default_e_min = self.parameters['e_min']['type'](self.parameters['e_min']['default'])
        self.default_e_max = self.parameters['e_max']['type'](self.parameters['e_max']['default'])

        for key, default_val in self.parameters.items():
            if key in kwargs.keys():
                setattr(self, key, kwargs[key])
            elif not hasattr(self, key) or getattr(self, key) is None:
                setattr(self, key, default_val['default'])

        self.delta = None
        self.analytical_delta = None
        self.closest_energy = None
        self.content = None
        self.raw_content = None

        if self.outfile:
            self.save_to_file()
            return

        if not self.data_file:
            self._request_from_server()

        if self.calc_delta:
            if self.available_libs['periodictable']:
                self.calculate_delta()
                self.delta = self.analytical_delta
            else:
                raise ValueError('periodictable library is not available. Install it if you want to use it.')
        else:
            self._find_delta()

        if self.verbose:
            self.print_info()

    def calculate_delta(self):
        rho = getattr(self.periodictable, self.formula).density
        z = getattr(self.periodictable, self.formula).number
        mass = getattr(self.periodictable, self.formula).mass
        z_over_a = z / mass
        wl = 2 * math.pi * 1973 / self.energy  # lambda= (2pi (hc))/E
        self.analytical_delta = 2.7e-6 * wl ** 2 * rho * z_over_a

    def print_info(self):
        msg = 'Found delta={} for the closest energy={} eV.'
        print(msg.format(self.delta, self.closest_energy))

    def save_to_file(self):
        self.e_min = self.default_e_min
        self.e_max = self.e_min
        counter = 0
        try:
            os.remove(self.outfile)
        except:
            pass
        while self.e_max < self.default_e_max:
            self.e_max += self.n_points * self.e_step
            if self.e_max > self.default_e_max:
                self.e_max = self.default_e_max

            self._request_from_server()

            if counter > 0:
                # Get rid of headers (2 first rows) and the first data row to avoid data overlap:
                content = self.content.split('\n')
                self.content = '\n'.join(content[3:])

            with open(self.outfile, 'a') as f:
                f.write(self.content)

            counter += 1
            self.e_min = self.e_max

        print('Data from {} eV to {} eV saved to the <{}> file.'.format(
            self.default_e_min, self.default_e_max, self.outfile))
        print('Energy step: {} eV, number of points/chunk: {}, number of chunks {}.'.format(
            self.e_step, self.n_points, counter))

    def _check_imports(self):
        self.available_libs = {
            'numpy': None,
            'periodictable': None,
            'requests': None,
        }
        for key in self.available_libs.keys():
            try:
                __import__(key)
                setattr(self, key, __import__(key))
                self.available_libs[key] = True
            except:
                self.available_libs[key] = False

    def _find_delta(self):
        skiprows = 2
        energy_column = 0
        delta_column = 1
        error_msg = 'Error! Use energy range from {} to {} eV.'
        if self.use_numpy and self.available_libs['numpy']:
            if self.data_file:
                data = self.numpy.loadtxt(self.data_file, skiprows=skiprows)

                self.default_e_min = data[0, energy_column]
                self.default_e_max = data[-1, energy_column]

                try:
                    idx_previous = self.numpy.where(data[:, energy_column] <= self.energy)[0][-1]
                    idx_next = self.numpy.where(data[:, energy_column] > self.energy)[0][0]
                except IndexError:
                    raise Exception(error_msg.format(self.default_e_min, self.default_e_max))

                idx = idx_previous if abs(data[idx_previous, energy_column] - self.energy) <= abs(
                    data[idx_next, energy_column] - self.energy) else idx_next

                self.delta = data[idx][delta_column]
                self.closest_energy = data[idx][energy_column]
            else:
                raise Exception('Processing with NumPy is only possible with the specified file, not content.')
        else:
            if not self.content:
                with open(self.data_file, 'r') as f:
                    self.raw_content = f.read()
            else:
                if type(self.content) != list:
                    self.raw_content = self.content

            self.content = self.raw_content.strip().split('\n')

            energies = []
            deltas = []
            for i in range(skiprows, len(self.content)):
                energies.append(float(self.content[i].split()[energy_column]))
                deltas.append(float(self.content[i].split()[delta_column]))

            self.default_e_min = energies[0]
            self.default_e_max = energies[-1]

            indices_previous = []
            indices_next = []
            try:
                for i in range(len(energies)):
                    if energies[i] <= self.energy:
                        indices_previous.append(i)
                    else:
                        indices_next.append(i)
                idx_previous = indices_previous[-1]
                idx_next = indices_next[0]
            except IndexError:
                raise Exception(error_msg.format(self.default_e_min, self.default_e_max))

            idx = idx_previous if abs(energies[idx_previous] - self.energy) <= abs(
                energies[idx_next] - self.energy) else idx_next

            self.delta = deltas[idx]
            self.closest_energy = energies[idx]

    def _get_file_content(self):
        get_url = '{}{}'.format(self.defaults['server'], self.file_name)
        r = self.requests.get(get_url)
        self.content = r.text

    def _get_file_name(self):
        if self.precise:
            e_min = self.energy - 1.0
            e_max = self.energy + 1.0
        else:
            e_min = self.e_min
            e_max = self.e_max
        payload = {
            'Density': -1,
            'Formula': self.formula,
            'Material': 'Enter Formula',
            'Min': e_min,
            'Max': e_max,
            'Npts': self.n_points,
            'Output': 'Text File',
            'Scan': 'Energy',
        }
        r = self.requests.post('{}{}'.format(self.defaults['server'], self.defaults['post_url']), payload)
        content = r.text

        # The file name should be something like '/tmp/xray2565.dat':
        try:
            self.file_name = str(content.split('URL=')[1].split('>')[0].replace('"', ''))
        except:
            raise Exception('\n\nFile name cannot be found! Server response:\n<{}>'.format(content.strip()))

    def _request_from_server(self):
        if self.available_libs['requests']:
            self._get_file_name()
            self._get_file_content()
        else:
            msg = 'Cannot use online resource <{}> to get delta. Use local file instead.'
            raise Exception(msg.format(self.defaults['server']))
