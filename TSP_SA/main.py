from parser import TSPParser
from distance_matrix import DistanceMatrix
from visualization import Visualizer
from evaluation import calculate_error_percent
from simulated_annealing import SimulatedAnnealing


OPTIMAL_SOLUTIONS = {
    "att532": 27686,
    "lin318": 42029,
    "p654": 34643,
    "rat575": 6773,
    "rd400": 15281
}


datasets = TSPParser.read_all("data")

visualizer = Visualizer()

print("\n" + "=" * 70)
print("SIMULATED ANNEALING - TSP")
print("=" * 70)

for tsp in datasets:

    print("\n" + "=" * 70)
    print(f"DATASET: {tsp.name}")
    print("=" * 70)

    matrix = DistanceMatrix(tsp)

    sa = SimulatedAnnealing(
        distance_matrix=matrix,

        initial_temperature=10000,

        cooling_rate=0.995,

        minimum_temperature=0.01,

        iterations_per_temperature=100
    )

    best_route, best_distance = sa.run()

    history = sa.get_history()

    routes_history, distances_history = (sa.get_routes_history())

    optimal = OPTIMAL_SOLUTIONS.get(tsp.name)

    print("\n" + "=" * 70)
    print("WYNIKI")
    print("=" * 70)

    print(f"\nNajlepsza długość trasy: {best_distance}")

    if optimal is not None:

        print(f"\nOptimum TSPLib: {optimal}")

        error = calculate_error_percent(best_distance, optimal)

        print(f"\nBłąd względem optimum: {error:.2f}%")

    else:

        print("\nBrak optimum dla datasetu.")

    print("\nFragment najlepszej trasy:")

    print(best_route[:20])

    print("\nGenerowanie wizualizacji...\n")

    # 1. Najlepsza trasa
    visualizer.plot_route(tsp=tsp, route=best_route, distance=best_distance, title=f"Best Route - {tsp.name}")

    # 2. Convergence plot
    visualizer.plot_convergence(history=history, dataset_name=tsp.name)

    # 3. Temperature plot
    visualizer.plot_temperature(history=history, dataset_name=tsp.name)

    # 4. Animacja krokowa
    visualizer.animate_route_evolution(tsp=tsp, routes_history=routes_history,distances_history=distances_history, interval=50)

    print("\nWizualizacje zapisane.")

    print("\n")

    print("\n")
