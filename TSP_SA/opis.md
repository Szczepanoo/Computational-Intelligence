## Zadanie 2 — Symulowane Wyżarzanie dla Problemu Komiwojażera (TSP)

### Autor projektu

* Jakub Szczepański

---

# Opis projektu

Celem projektu była implementacja algorytmu symulowanego wyżarzania (Simulated Annealing, SA) służącego do rozwiązywania problemu komiwojażera (Travelling Salesman Problem, TSP).

Projekt został wykonany bez wykorzystania gotowych bibliotek optymalizacyjnych. Implementacja obejmuje:

* parser danych TSPLib,
* generowanie macierzy odległości,
* implementację algorytmu SA,
* implementację operatorów modyfikacji trasy,
* wizualizację tras,
* animację przebiegu działania algorytmu,
* analizę jakości rozwiązania względem optimum TSPLib.

Program został przetestowany na pięciu instancjach problemu TSP:

* att532
* lin318
* p654
* rat575
* rd400

---

# Reprezentacja rozwiązania

Trasa reprezentowana jest jako permutacja indeksów miast.

Przykład:

```text
[0, 5, 2, 1, 3, 4]
```

Każde miasto występuje dokładnie jeden raz.

---

# Zastosowane operatory zmiany trasy

W projekcie zaimplementowano cztery operatory zmiany trasy:

1. Swap
   Zamiana dwóch losowych miast miejscami.

2. Insert
   Usunięcie miasta i wstawienie go w inne miejsce trasy.

3. Inversion
   Odwrócenie fragmentu trasy.

4. Segment Shift
   Przeniesienie fragmentu trasy w inne miejsce.

---

# Opis działania algorytmu

Algorytm rozpoczyna działanie od wygenerowania losowej trasy początkowej.

W każdej iteracji:

* generowane jest rozwiązanie sąsiednie,
* obliczana jest długość nowej trasy,
* sprawdzane jest prawdopodobieństwo akceptacji nowego rozwiązania,
* temperatura jest stopniowo zmniejszana zgodnie z harmonogramem chłodzenia.

Algorytm kończy działanie po osiągnięciu minimalnej temperatury lub maksymalnej liczby iteracji.

---

# Pseudokod algorytmu symulowanego wyżarzania

```text
ALGORYTM SimulatedAnnealing

WEJŚCIE:
    distance_matrix
    initial_temperature
    cooling_rate
    minimum_temperature
    iterations_per_temperature

WYJŚCIE:
    best_route
    best_distance


current_route = generate_random_route()

current_distance = calculate_route_distance(current_route)

best_route = current_route
best_distance = current_distance

temperature = initial_temperature

iteration = 0


WHILE temperature > minimum_temperature DO:

    FOR i = 1 TO iterations_per_temperature DO:

        operator = choose_random_operator()

        new_route = operator(current_route)

        new_distance = calculate_route_distance(new_route)

        IF new_distance < current_distance THEN:

            current_route = new_route
            current_distance = new_distance

        ELSE:

            delta = new_distance - current_distance

            probability = exp(-delta / temperature)

            random_value = random(0, 1)

            IF random_value < probability THEN:

                current_route = new_route
                current_distance = new_distance

            END IF

        END IF


        IF current_distance < best_distance THEN:

            best_route = current_route
            best_distance = current_distance

        END IF


        save_history(iteration, temperature, current_distance, best_distance)

        iteration = iteration + 1

    END FOR


    temperature = temperature * cooling_rate

END WHILE


RETURN best_route, best_distance
```

---

# Pseudokod operatora SWAP

```text
ALGORYTM SwapOperator

WEJŚCIE:
    route

WYJŚCIE:
    modified_route


new_route = copy(route)

i, j = dwa losowe indeksy

swap(new_route[i], new_route[j])

RETURN new_route
```

---

# Pseudokod operatora INSERT

```text
ALGORYTM InsertOperator

WEJŚCIE:
    route

WYJŚCIE:
    modified_route


new_route = copy(route)

i, j = dwa losowe indeksy

city = remove(new_route[i])

insert city at position j

RETURN new_route
```

---

# Pseudokod operatora INVERSION

```text
ALGORYTM InversionOperator

WEJŚCIE:
    route

WYJŚCIE:
    modified_route


new_route = copy(route)

start, end = dwa losowe indeksy

reverse(fragment od start do end)

RETURN new_route
```

---

# Pseudokod operatora SEGMENT SHIFT

```text
ALGORYTM SegmentShiftOperator

WEJŚCIE:
    route

WYJŚCIE:
    modified_route


new_route = copy(route)

start, end = dwa losowe indeksy

segment = fragment trasy

remove segment from route

insert_position = losowa pozycja

insert segment into route

RETURN new_route
```

---

# Wizualizacja

Projekt zawiera:

* wizualizację końcowej trasy,
* wykres zbieżności algorytmu,
* wykres temperatury,
* animację krokowego działania algorytmu.

---

# Wnioski

Algorytm symulowanego wyżarzania pozwala skutecznie poprawiać jakość rozwiązań problemu TSP poprzez kontrolowane akceptowanie gorszych rozwiązań na początkowych etapach działania.

Zastosowane operatory umożliwiają eksplorację przestrzeni rozwiązań i stopniowe znajdowanie coraz krótszych tras.
