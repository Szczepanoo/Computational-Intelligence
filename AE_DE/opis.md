## Zadanie 1 — Algorytmy Ewolucyjne i Ewolucja Różnicowa

### Autor projektu

* Jakub Szczepański

---

# Opis projektu

W ramach projektu zaimplementowano dwa algorytmy optymalizacji:

* algorytm ewolucyjny (AE),
* ewolucję różnicową (Differential Evolution, DE). 


Algorytm ewolucyjny wykorzystuje:

* selekcję turniejową,
* crossover arytmetyczny,
* mutację gaussowską,
* mechanizm elityzmu. 

Populacja początkowa generowana jest losowo w zadanym zakresie wartości. W każdej iteracji obliczana jest wartość funkcji celu dla wszystkich osobników, a następnie tworzona jest nowa populacja potomna. 

Algorytm Differential Evolution został zaimplementowany w wariancie DE/rand/1/bin. Mutacja realizowana jest zgodnie ze wzorem:

v=a+F(b-c)

gdzie:

* `a` jest osobnikiem bazowym,
* `b` i `c` są losowo wybranymi osobnikami populacji,
* `F` oznacza współczynnik mutacji. 

Do testów wykorzystano pięć funkcji benchmarkowych:

* Sphere,
* Rastrigin,
* Rosenbrock,
* Ackley,
* Griewank. 

Testy przeprowadzono dla problemów wielowymiarowych (50 wymiarów). Dodatkowo przygotowano wizualizację działania algorytmów dla funkcji dwuwymiarowych z wykorzystaniem biblioteki Plotly. 

W każdej iteracji zapisywano:

* najlepszy fitness,
* średni fitness,
* najgorszy fitness populacji. 

Wyniki eksportowane są do plików CSV, co umożliwia dalszą analizę oraz porównanie skuteczności algorytmów AE i DE. 

---

# Reprezentacja osobnika

Osobnik reprezentowany jest jako wektor liczb rzeczywistych.

Przykład:

```text id="q1fnd0"
[1.25, -3.14, 0.78, 5.91, ...]
```

Każdy element wektora odpowiada jednej zmiennej optymalizacyjnej funkcji celu.

---

# Opis działania algorytmu ewolucyjnego

Algorytm rozpoczyna działanie od wygenerowania losowej populacji osobników.

W każdej generacji:

* obliczany jest fitness wszystkich osobników,
* wybierani są rodzice metodą selekcji turniejowej,
* wykonywany jest crossover,
* wykonywana jest mutacja,
* tworzona jest nowa populacja.

Najlepsze osobniki przekazywane są do kolejnej generacji przy pomocy mechanizmu elityzmu.

---

# Pseudokod algorytmu ewolucyjnego

```text id="n7v1mz"
Algorithm EvolutionaryAlgorithm

Input:
    func
    dimensions
    bounds
    pop_size
    generations
    mutation_rate
    mutation_strength
    elite_size

Output:
    best_solution
    best_fitness


population = losowa populacja(pop_size, dimensions, bounds)

FOR generation = 1 TO generations DO:

    fitness = evaluate(population, func)

    best = minimum(fitness)
    mean = średnia(fitness)
    worst = maksimum(fitness)

    elite_indices = indeksy najlepszych elite_size osobników

    new_population = elity z population

    WHILE size(new_population) < pop_size DO:

        parent1 = tournament_selection(population, fitness)

        parent2 = tournament_selection(population,fitness)

        child = crossover(parent1, parent2)

        FOR i = 1 TO dimensions DO:

            IF random() < mutation_rate THEN:

                child[i] = child[i] + normal_random(0, mutation_strength)

            END IF

        END FOR

        child = clip(child, bounds)

        add child to new_population

    END WHILE

    population = new_population

END FOR

final_fitness = evaluate(population, func)

best_index = indeks najlepszego osobnika

best_solution = population[best_index]

best_fitness = final_fitness[best_index]

RETURN best_solution, best_fitness
```

---

# Opis działania algorytmu Differential Evolution

Algorytm DE rozpoczyna działanie od wygenerowania losowej populacji.

Dla każdego osobnika:

* wybierane są trzy losowe osobniki populacji,
* generowany jest wektor mutant,
* wykonywany jest crossover binarny,
* tworzony jest wektor próbny,
* wybierane jest lepsze rozwiązanie.

Proces powtarzany jest przez określoną liczbę generacji.

---

# Pseudokod algorytmu Differential Evolution

```text id="j4k4kl"
Algorithm DifferentialEvolution

Input:
    func
    dimensions
    bounds
    pop_size
    generations
    F
    CR

Output:
    best_solution
    best_fitness


population = losowa populacja(pop_size, dimensions, bounds)

FOR generation = 1 TO generations DO:

    fitness = evaluate(population, func)

    best = minimum(fitness)
    mean = średnia(fitness)
    worst = maksimum(fitness)

    new_population = empty

    FOR i = 1 TO pop_size DO:

        target = population[i]

        wybierz losowo: a, b, c

        mutant = a + F * (b - c)

        mutant = clip(mutant, bounds)

        trial = copy(target)

        random_index = losowy indeks wymiaru

        FOR j = 1 TO dimensions DO:

            IF random() < CR OR j = random_index THEN:

                trial[j] = mutant[j]

            END IF

        END FOR

        IF func(trial) < func(target) THEN:

            add trial to new_population

        ELSE:

            add target to new_population

        END IF

    END FOR

    population = new_population

END FOR

final_fitness = evaluate(population, func)

best_index = indeks najlepszego osobnika

best_solution = population[best_index]

best_fitness = final_fitness[best_index]

RETURN best_solution, best_fitness
```

---

# Wizualizacja

Projekt zawiera:

* wizualizację funkcji benchmarkowych,
* wizualizację położenia osobników,
* wykresy zmian fitness w kolejnych iteracjach,
* porównanie działania algorytmu AE i DE.

---

# Wnioski

Oba algorytmy umożliwiają skuteczną optymalizację funkcji wielowymiarowych.

Algorytm ewolucyjny charakteryzuje się większą eksploracją przestrzeni rozwiązań dzięki mutacji i crossoverowi, natomiast Differential Evolution szybciej osiąga dobre rozwiązania dzięki mechanizmowi różnicowej mutacji.

Największy wpływ na skuteczność algorytmów miały:

* rozmiar populacji,
* współczynnik mutacji,
* liczba generacji,
* parametry crossoveru,
* mechanizm selekcji.
