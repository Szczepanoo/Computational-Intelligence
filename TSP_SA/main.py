from parser import TSPParser
from distance_matrix import DistanceMatrix

datasets = TSPParser.read_all("data")

for d in datasets:
    tsp = d

    matrix = DistanceMatrix(tsp)

    matrix.print_info()
    matrix.print_sample()

    print("\nPrzykładowe odległości:\n")

    print(f"0 -> 1 = {matrix.get_distance(0, 1)}")
    print(f"1 -> 2 = {matrix.get_distance(1, 2)}")
    print(f"2 -> 3 = {matrix.get_distance(2, 3)}")