'''
    Read CSV data with Pandas #2
'''

import pandas as pd


def read_csv(url):
    '''
        Read in function
    '''
    return pd.read_csv(url, header=None, names=['x', 'y'])
