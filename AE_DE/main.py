from functions import FUNCTIONS
from evolutionary import evolutionary_algorithm
from differential import differential_evolution
from visualization import visualize_population_steps

for f in FUNCTIONS:
    FUNCTION = FUNCTIONS[f]

    print("Evolutionary algorithm")

    print("\n" + "=" * 50)
    print("Function: sphere")
    print("")
    ae_result = evolutionary_algorithm(
        func=FUNCTION,
        dimensions=2,
        bounds=(-10, 10),
        pop_size=10,
        generations=20
    )

    print("Best fitness:")
    print(ae_result["best_fitness"])

    print("\nBest solution:")
    print(ae_result["best_solution"])


    last_population = ae_result["population"]

    visualize_population_steps(
        FUNCTION,
        ae_result["history"],
        (-10, 10)
    )


    print()
    print()
    print()
    print()
    print()
    print("Differential evolution")
    print()

    print("\n" + "=" * 50)
    print("Function: sphere")
    print("")
    de_result = differential_evolution(
        func=FUNCTION,
        dimensions=2,
        bounds=(-5, 5),
        pop_size=10,
        generations=20
    )

    print("Best fitness:")
    print(de_result["best_fitness"])

    print("\nBest solution:")
    print(de_result["best_solution"])


    visualize_population_steps(
        FUNCTION,
        de_result["history"],
        (-10, 10)
    )