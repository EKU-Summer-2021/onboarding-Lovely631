'''
    Read CSV data with Pandas #2 - Test
'''

import unittest

import pandas as pd

from src.csv_read_data import read_csv


class CsvReadDataTest(unittest.TestCase):
    '''
        CSV read in test
    '''

    def test_read_csv(self):
        '''
            Unit test for csv read in
        '''
        # given
        expected = True
        # when
        actual = isinstance(read_csv('https://raw.githubusercontent.com/EKU-Summer-2021/'
                                     'intelligent_system_data/main/'
                                     'Intelligent%20System%20Data/TSP/10.csv'), pd.DataFrame)
        # then
        self.assertEqual(expected, actual)
