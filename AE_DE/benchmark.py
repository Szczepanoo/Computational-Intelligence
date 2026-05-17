from functions import FUNCTIONS
from evolutionary import evolutionary_algorithm
from differential import differential_evolution
from report import generate_reports, finalize_summary

summary_rows = []

for name, func in FUNCTIONS.items():

    print("\n" + "=" * 50)
    print("Function:", name)
    print()
    print("Evolutionary algorithm")
    print()
    ae_result = evolutionary_algorithm(
        func=func,
        dimensions=50,
        bounds=(-5, 5),
        pop_size=50,
        generations=200
    )

    print("Best fitness:")
    print(ae_result["best_fitness"])

    print("\nBest solution:")
    print(ae_result["best_solution"])

    print()
    print("Differential Evolution...")
    print()

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

    generate_reports(
        function_name=name,
        ae_result=ae_result,
        de_result=de_result,
        summary_rows=summary_rows
    )

finalize_summary(summary_rows)

print()
print("=" * 50)
print("All reports generated.")
print("=" * 50)
