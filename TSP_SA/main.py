from parser import TSPParser
from distance_matrix import DistanceMatrix
from evaluation import generate_random_route, print_route, validate_route, calculate_error_percent, calculate_route_distance

datasets = TSPParser.read_all("data")

OPTIMAL_SOLUTIONS = {
    "att532": 27686,
    "lin318": 42029,
    "p654": 34643,
    "rat575": 6773,
    "rd400": 15281
}


for tsp in datasets:

    matrix = DistanceMatrix(tsp)

    route = generate_random_route(tsp.dimension)

    print("=" * 50)
    print(f"TEST ROUTE: {tsp.name}")

    print("\nFragment trasy:")
    print_route(route)

    is_valid = validate_route(route, tsp.dimension)

    print(f"\nCzy trasa poprawna? {is_valid}")

    distance = calculate_route_distance(route, matrix)

    print(f"\nDługość trasy: {distance}")
    
    optimal = OPTIMAL_SOLUTIONS.get(tsp.name)

    print(f"\nOptimum: {optimal}")
    
    error = calculate_error_percent(distance, optimal)

    print(f"\nBłąd względem optimum: {error:.2f}%")
    