import random


def swap_operator(route: list[int]) -> list[int]:

    new_route = route.copy()

    i, j = random.sample(range(len(route)), 2)

    new_route[i], new_route[j] = (new_route[j], new_route[i])

    return new_route


def insert_operator(route: list[int]) -> list[int]:

    new_route = route.copy()

    i, j = random.sample(range(len(route)), 2)

    city = new_route.pop(i)
    
    new_route.insert(j, city)

    return new_route


def inversion_operator(route: list[int]) -> list[int]:

    new_route = route.copy()

    i, j = sorted(random.sample(range(len(route)), 2))

    new_route[i:j + 1] = reversed(new_route[i:j + 1])

    return new_route


def segment_shift_operator(route: list[int]) -> list[int]:

    size = len(route)

    new_route = route.copy()

    start, end = sorted(random.sample(range(size), 2))

    segment = new_route[start:end + 1]

    remaining = (new_route[:start] + new_route[end + 1:])

    insert_pos = random.randint(0, len(remaining))

    shifted_route = (remaining[:insert_pos] + segment + remaining[insert_pos:])

    return shifted_route


def random_operator(route: list[int]) -> tuple[str, list[int]]:

    operator_name, operator_func = random.choice(OPERATORS)

    new_route = operator_func(route)

    return operator_name, new_route


OPERATORS = [
        ("SWAP", swap_operator),
        ("INSERT", insert_operator),
        ("INVERSION", inversion_operator),
        ("SEGMENT_SHIFT", segment_shift_operator)
    ]
