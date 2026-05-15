import numpy as np

def initialize_population(pop_size, dimensions, bounds):
    low, high = bounds

    return np.random.uniform(
        low,
        high,
        (pop_size, dimensions)
    )


def evaluate_population(population, func):
    return np.array([
        func(individual)
        for individual in population
    ])


def differential_evolution(func, dimensions, bounds, pop_size=50,
                           generations=100, F=0.5, CR=0.7):

    population = initialize_population(pop_size, dimensions, bounds)

    history = []

    for generation in range(generations):

        fitness = evaluate_population(population, func)

        best = np.min(fitness)
        mean = np.mean(fitness)
        worst = np.max(fitness)

        history.append({
            "generation": generation,
            "best": best,
            "mean": mean,
            "worst": worst
        })

        new_population = []

        for i in range(pop_size):

            target = population[i]

            indices = list(range(pop_size))
            indices.remove(i)

            a_idx, b_idx, c_idx = np.random.choice(indices, 3, replace=False)

            a = population[a_idx]
            b = population[b_idx]
            c = population[c_idx]

            mutant = a + F * (b - c)

            mutant = np.clip(mutant, bounds[0], bounds[1])

            trial = target.copy()

            random_index = np.random.randint(dimensions)

            for j in range(dimensions):

                if np.random.rand() < CR or j == random_index:
                    trial[j] = mutant[j]

            if func(trial) < func(target):
                new_population.append(trial)
            else:
                new_population.append(target)

        population = np.array(new_population)

        if (generation % 10 == 0):
            print(f"Generation {generation} | Best: {best:.8f} | Mean: {mean:.8f}")

    final_fitness = evaluate_population(population, func)

    best_index = np.argmin(final_fitness)

    best_solution = population[best_index]

    return {
        "best_solution": best_solution,
        "best_fitness": final_fitness[best_index],
        "history": history,
        "population": population
    }