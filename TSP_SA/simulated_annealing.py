import math
import random

from evaluation import generate_random_route, calculate_route_distance
from operators import random_operator


class SimulatedAnnealing:

    def __init__(self, distance_matrix, initial_temperature: float = 10000.0,
                 cooling_rate: float = 0.995, minimum_temperature: float = 0.001,
                 iterations_per_temperature: int = 100):

        self.distance_matrix = distance_matrix
        self.num_cities = distance_matrix.dimension
        
        self.initial_temperature = initial_temperature
        self.cooling_rate = cooling_rate
        self.minimum_temperature = minimum_temperature

        self.iterations_per_temperature = iterations_per_temperature

        self.routes_history = []
        self.distances_history = []

        self.history = {"iteration": [], "temperature": [], 
                        "current_distance": [],"best_distance": []}

    def initialize_solution(self):

        route = generate_random_route(self.num_cities)

        distance = calculate_route_distance(route, self.distance_matrix)

        return route, distance

    @staticmethod
    def acceptance_probability(current_distance: float, new_distance: float, temperature: float) -> float:

        if new_distance < current_distance:
            return 1.0

        delta = (new_distance- current_distance)

        return math.exp(-delta / temperature)

    def cool_down(self, temperature: float) -> float:

        return (temperature * self.cooling_rate)

    def save_history(self, iteration, temperature, current_distance, best_distance):

        self.history["iteration"].append(iteration)

        self.history["temperature"].append(temperature)

        self.history["current_distance"].append(current_distance)

        self.history["best_distance"].append(best_distance)

    def run(self):

        current_route, current_distance = (self.initialize_solution())

        best_route = current_route.copy()
        best_distance = current_distance

        temperature = (self.initial_temperature)

        iteration = 0

        print("\n" + "=" * 60)
        print("START SIMULATED ANNEALING")
        print("=" * 60)

        print(f"\nInitial distance: {current_distance}")

        while temperature > self.minimum_temperature:

            for _ in range(self.iterations_per_temperature):

                operator_name, new_route = (random_operator(current_route))

                new_distance = (calculate_route_distance(new_route, self.distance_matrix))

                probability = (self.acceptance_probability(current_distance, new_distance, temperature))
                
                if random.random() < probability:

                    current_route = new_route
                    current_distance = new_distance

                if current_distance < best_distance:

                    best_route = (current_route.copy())

                    best_distance = (current_distance)

                self.save_history(iteration, temperature, current_distance, best_distance)

                if iteration % 100 == 0:
                    self.routes_history.append(best_route.copy())

                    self.distances_history.append(best_distance)

                if iteration % 1000 == 0:

                    print(f"Iteracja: {iteration:>7} | T: {temperature:>10.4f} | "
                          f"Current: {current_distance:>10} | Best: {best_distance:>10} | Operator: {operator_name}")

                iteration += 1

            # Chłodzenie
            temperature = self.cool_down(temperature)

        print("\n" + "=" * 60)
        print("KONIEC SYMULOWANEGO WYŻARZANIA")
        print("=" * 60)

        print(f"\nBest distance found: {best_distance}")

        return best_route, best_distance

    def get_history(self):

        return self.history
    
    
    def get_routes_history(self):

        return (self.routes_history, self.distances_history)
