'''
    City class for tsp problem
'''
from dataclasses import dataclass


@dataclass
class City:
    '''
        Class to city
    '''

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def __repr__(self) -> str:
        return '({},{})'.format(self.x_coordinate, self.y_coordinate)
