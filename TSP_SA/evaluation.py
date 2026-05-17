import random
from distance_matrix import DistanceMatrix


def generate_random_route(num_cities: int) -> list[int]:
    
    route = list(range(num_cities))
    random.shuffle(route)

    return route


def validate_route(route: list[int], num_cities: int) -> bool:

    if len(route) != num_cities:
        return False

    if len(set(route)) != num_cities:
        return False

    if min(route) < 0:
        return False

    if max(route) >= num_cities:
        return False

    return True


def calculate_route_distance(route: list[int],distance_matrix: DistanceMatrix) -> int:

    total_distance = 0

    for i in range(len(route) - 1):

        city_a = route[i]
        city_b = route[i + 1]

        total_distance += distance_matrix.get_distance(city_a, city_b)

    # Domknięcie cyklu
    total_distance += distance_matrix.get_distance(route[-1], route[0])

    return total_distance


def calculate_error_percent(found_distance: float,optimal_distance: float) -> float:

    return ((found_distance - optimal_distance) / optimal_distance) * 100.0


def print_route(route: list[int], max_cities: int = 20) -> None:

    if len(route) <= max_cities:
        print(route)
    else:
        preview = route[:max_cities]
        print(f"{preview} ...")

