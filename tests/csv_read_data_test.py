import unittest
import pandas as pd
from src.csv_read_data import read_csv


class CsvReadDataTest(unittest.TestCase):

    def test_read_in_should_be_csv(self):
        # given
        expected = True
        # when
        actual = isinstance(read_csv('https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/main/Intelligent%20System%20Data/CSP/CSP_360.csv'), pd.DataFrame)
        # then
        self.assertEqual(expected, actual)
