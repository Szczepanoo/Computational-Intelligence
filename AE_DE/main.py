from functions import sphere
from evolutionary import evolutionary_algorithm

result = evolutionary_algorithm(
    func=sphere,
    dimensions=10,
    bounds=(-5, 5),
    pop_size=50,
    generations=200
)

print("Best fitness:")
print(result["best_fitness"])

print("\nBest solution:")
print(result["best_solution"])