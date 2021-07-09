'''
    Create cost function for genetic algorithm #3
'''
import numpy as np

from src.city import City


class Tsp():
    '''
        Class to tsp
    '''

    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.city_list = self.__dataframe_to_list()

    def __dataframe_to_list(self):
        '''
            Convert dataframe to list
        '''

        city_list = []
        for _, row in self.dataframe.iterrows():
            city_list.append(City(row['x'], row['y']))
        return city_list

    def euclidean_distance(self, index_1, index_2):
        '''
            Calculates two city (index_1.x index_1.y and index_2.x index_2.y) distance
        '''

        # d = sqrt[(x2 – x1)**2 + (y2 – y1)**2]
        return np.sqrt(
            (self.city_list[index_1].x_coordinate - self.city_list[index_2].x_coordinate) ** 2 +
            (self.city_list[index_1].y_coordinate - self.city_list[index_2].y_coordinate) ** 2)

    def cost_function(self, city_config):
        '''
            Calculates all of the city distances with the given values to the city_config
             meaning that the city_config requires an array of numbers
             that represents which order we travel around of the cities
        '''

        sum_of_cost = 0
        for i in range(len(city_config) - 1):
            sum_of_cost += self.euclidean_distance(city_config[i], city_config[i + 1])
        return sum_of_cost
