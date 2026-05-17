import numpy as np


def sphere(x):
    return np.sum(x ** 2)


def rastrigin(x):
    n = len(x)
    return 10 * n + np.sum(x**2 - 10 * np.cos(2 * np.pi * x))


def rosenbrock(x):
    return np.sum(100 * (x[1:] - x[:-1]**2)**2 + (x[:-1] - 1)**2)


def ackley(x):
    n = len(x)

    term1 = -20 * np.exp(-0.2 * np.sqrt(np.sum(x**2) / n))

    term2 = -np.exp(np.sum(np.cos(2 * np.pi * x)) / n)

    return term1 + term2 + 20 + np.e


def griewank(x):
    n = len(x)

    sum_part = np.sum(x**2) / 4000

    prod_part = np.prod([np.cos(x[i] / np.sqrt(i + 1)) for i in range(n)])

    return 1 + sum_part - prod_part


FUNCTIONS = {
    "sphere": sphere,
    "rastrigin": rastrigin,
    "rosenbrock": rosenbrock,
    "ackley": ackley,
    "griewank": griewank
}