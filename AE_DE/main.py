from functions import FUNCTIONS, sphere, griewank, rastrigin
from evolutionary import evolutionary_algorithm
from differential import differential_evolution
from visualization import plot_convergence, plot_population_3d, animate_population, visualize_population_steps

for f in FUNCTIONS:
    FUNCTION = FUNCTIONS[f]

    print("Evolutionary algorithm")

    print("\n" + "=" * 50)
    print("Function: sphere")
    print("")
    ea_result = evolutionary_algorithm(
        func=FUNCTION,
        dimensions=2,
        bounds=(-10, 10),
        pop_size=10,
        generations=20
    )

    print("Best fitness:")
    print(ea_result["best_fitness"])

    print("\nBest solution:")
    print(ea_result["best_solution"])


    last_population = ea_result["population"]

    # plot_population_3d(
    #     sphere,
    #     last_population,
    #     (-5, 5)
    # )

    visualize_population_steps(
        FUNCTION,
        ea_result["history"],
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