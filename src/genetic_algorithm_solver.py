'''
    Module for solving problems with Genetic Algorithm
'''

import numpy as np


class GeneticAlgorithmSolver():
    '''
        Class for solving problems with Genetic Algorithm
    '''

    def __init__(self, tsp):
        self.tsp = tsp
        self.random_cities = self.multiple_random_order_of_cities()
        self.min_cost = self.evaluation()
        self.best_routes = self.find_city_route_by_cost()

    def __random_order_of_cities(self):
        '''
            Creates a random route
        '''

        randomized_array_of_cities = np.random.permutation(10)
        to_list = randomized_array_of_cities.tolist()
        return to_list

    def multiple_random_order_of_cities(self):
        '''
            Creates 10 randomized city route
        '''

        index = 1
        list_of_randomized_cities = []
        while index < 10:
            list_of_randomized_cities.append(self.__random_order_of_cities())
            index = index + 1
        self.random_cities = list_of_randomized_cities
        return list_of_randomized_cities

    def evaluation(self, list_of_paths=None):
        '''
            Calculates the cost of the random routes
        '''

        if list_of_paths is None:
            list_of_paths = self.random_cities
        cost_list = []
        for path in list_of_paths:
            cost_list.append(self.tsp.cost_function(path))
        return cost_list

    def minimum_cost(self):
        '''
            From the calculated cost we take 2 least "expensive" route
        '''

        minimum_cost = np.sort(self.evaluation())
        minimum_cost_list = minimum_cost.tolist()[:2]
        return minimum_cost_list

    def find_city_route_by_cost(self):
        '''
            Finds the best routes
        '''

        evaluation_values = np.array(self.evaluation())
        temp = np.array(self.random_cities)
        return temp[evaluation_values.argsort()][:2]

    def swap(self, route, position_1, position_2):
        '''
            Swapping elements at given positions
        '''
        route[position_1], route[position_2] = route[position_2], route[position_1]
        return route
