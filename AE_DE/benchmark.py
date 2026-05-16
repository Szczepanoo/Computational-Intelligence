from functions import FUNCTIONS, sphere
from evolutionary import evolutionary_algorithm
from differential import differential_evolution
from visualization import plot_convergence, plot_population_3d, animate_population, visualize_population_steps

print("Evolutionary algorithm")

for name, func in FUNCTIONS.items():
    print("\n" + "=" * 50)
    print("Function:",name)
    print("")
    ea_result = evolutionary_algorithm(
        func=func,
        dimensions=50,
        bounds=(-5, 5),
        pop_size=50,
        generations=200
    )

    print("Best fitness:")
    print(ea_result["best_fitness"])

    print("\nBest solution:")
    print(ea_result["best_solution"])


print()
print()
print()
print()
print()
print("Differential evolution")
print()

for name, func in FUNCTIONS.items():
    print("\n" + "=" * 50)
    print("Function:",name)
    print("")
    de_result = differential_evolution(
        func=func,
        dimensions=50,
        bounds=(-5, 5),
        pop_size=50,
        generations=200
    )

    print("Best fitness:")
    print(de_result["best_fitness"])

    print("\nBest solution:")
    print(de_result["best_solution"])
