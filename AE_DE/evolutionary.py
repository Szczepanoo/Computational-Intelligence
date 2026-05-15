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


def tournament_selection(population, fitness, k=3):
    indices = np.random.choice(
        len(population),
        k,
        replace=False
    )

    best_idx = indices[np.argmin(fitness[indices])]

    return population[best_idx]


def crossover(parent1, parent2):
    alpha = np.random.rand()

    child = (
        alpha * parent1 +
        (1 - alpha) * parent2
    )

    return child


def mutate(individual, mutation_rate, mutation_strength):
    mutated = individual.copy()

    for i in range(len(mutated)):
        if np.random.rand() < mutation_rate:
            mutated[i] += np.random.normal(
                0,
                mutation_strength
            )

    return mutated


def evolutionary_algorithm(func, dimensions, bounds, pop_size=50, generations=100,
                           mutation_rate=0.1,mutation_strength=0.1, elite_size=2):
    
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

        elite_indices = np.argsort(fitness)[:elite_size]

        new_population = [population[i] for i in elite_indices]

        while len(new_population) < pop_size:

            parent1 = tournament_selection(population, fitness)

            parent2 = tournament_selection(population, fitness)

            child = crossover(parent1,parent2)

            child = mutate(child,mutation_rate,mutation_strength)

            child = np.clip(child,bounds[0],bounds[1])

            new_population.append(child)

        population = np.array(new_population)

        final_fitness = evaluate_population(population, func)

        best_index = np.argmin(final_fitness)

        best_solution = population[best_index]

        if (generation % 10 == 0):
            print(f"Generation {generation} | Best: {best:.8f} | Mean: {mean:.8f}")

    return {
        "best_solution": best_solution,
        "best_fitness": final_fitness[best_index],
        "history": history,
        "population": population
    }