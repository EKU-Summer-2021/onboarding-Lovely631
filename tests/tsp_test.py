'''
    Create cost function for genetic algorithm #3 - Test
'''

import unittest

import numpy as np

from src.csv_read_data import read_csv
from src.tsp import Tsp


class TspTest(unittest.TestCase):
    '''
        TSP test
    '''

    def test_euclidean_distance(self):
        '''
            Unit test for two city distance calculator
        '''

        # given
        dataframe = read_csv('https://raw.githubusercontent.com/EKU-Summer-2021/'
                             'intelligent_system_data/main/Intelligent%20System%20Data/TSP/10.csv')
        tsp_instance = Tsp(dataframe)
        value = np.sqrt((dataframe.iloc[0, 0] - dataframe.iloc[1, 0]) ** 2 +
                        (dataframe.iloc[0, 1] - dataframe.iloc[1, 1]) ** 2)
        # np.sqrt((30-10)**2 + (64-37)**2)
        expected = value
        # when
        actual = tsp_instance.euclidean_distance(0, 1)
        # then
        self.assertEqual(expected, actual)

    def test_cost_function(self):
        '''
            Unit test for the cost function
        '''
        # given
        dataframe = read_csv('https://raw.githubusercontent.com/EKU-Summer-2021/'
                             'intelligent_system_data/main/Intelligent%20System%20Data/TSP/10.csv')
        tsp_instance = Tsp(dataframe)
        # order_of_cities = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = 402.98782258884467  # !!!!!
        # when
        actual = tsp_instance.cost_function([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        # then
        self.assertEqual(expected, actual)
