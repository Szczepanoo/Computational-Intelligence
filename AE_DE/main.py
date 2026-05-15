from functions import FUNCTIONS
from evolutionary import evolutionary_algorithm
from differential import differential_evolution

print("Evolutionary algorithm")

for name, func in FUNCTIONS.items():
    print("\n" + "=" * 50)
    print("Function:",name)
    print("")
    result = evolutionary_algorithm(
        func=func,
        dimensions=30,
        bounds=(-5, 5),
        pop_size=50,
        generations=100
    )

    print("Best fitness:")
    print(result["best_fitness"])

    print("\nBest solution:")
    print(result["best_solution"])

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
    result = differential_evolution(
        func=func,
        dimensions=30,
        bounds=(-5, 5),
        pop_size=50,
        generations=100
    )

    print("Best fitness:")
    print(result["best_fitness"])

    print("\nBest solution:")
    print(result["best_solution"])
