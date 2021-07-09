'''
    Main for tsp
'''

from src.csv_read_data import read_csv
from src.tsp import Tsp

# from src.genetic_algorithm_solver import GeneticAlgorithmSolver

if __name__ == '__main__':
    dataframe = read_csv('https://raw.githubusercontent.com/EKU-Summer-2021/'
                         'intelligent_system_data/main/Intelligent%20System%20Data/TSP/10.csv')

    # print(dataframe)

    tsp = Tsp(dataframe)
    print(tsp.city_list)
    city_list = tsp.city_list

    # genetic = GeneticAlgorithmSolver()

    # ga_solver = genetic.multiple_random_order_of_cities()
