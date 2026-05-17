import math
from typing import List

from parser import TSPInstance


class DistanceMatrix:

    def __init__(self, tsp_instance: TSPInstance):

        self.name = tsp_instance.name
        self.dimension = tsp_instance.dimension
        self.edge_weight_type = tsp_instance.edge_weight_type
        self.coordinates = tsp_instance.coordinates

        self.matrix = self._build_matrix()

    def _build_matrix(self) -> List[List[int]]:

        size = self.dimension

        matrix = [
            [0 for _ in range(size)]
            for _ in range(size)
        ]

        for i in range(size):

            _, x1, y1 = self.coordinates[i]

            for j in range(i + 1, size):

                _, x2, y2 = self.coordinates[j]

                distance = self._calculate_distance(
                    x1, y1,
                    x2, y2
                )

                matrix[i][j] = distance
                matrix[j][i] = distance

        return matrix

    def _calculate_distance(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float
    ) -> int:

        if self.edge_weight_type == "EUC_2D":
            return self._euclidean_distance(x1, y1, x2, y2)

        elif self.edge_weight_type == "ATT":
            return self._att_distance(x1, y1, x2, y2)

        else:
            raise ValueError(
                f"Nieobsługiwany typ odległości: "
                f"{self.edge_weight_type}"
            )

    @staticmethod
    def _euclidean_distance(
        x1: float,
        y1: float,
        x2: float,
        y2: float
    ) -> int:

        distance = math.sqrt(
            (x1 - x2) ** 2 +
            (y1 - y2) ** 2
        )

        return round(distance)

    @staticmethod
    def _att_distance(
        x1: float,
        y1: float,
        x2: float,
        y2: float
    ) -> int:

        dx = x1 - x2
        dy = y1 - y2

        rij = math.sqrt(
            (dx * dx + dy * dy) / 10.0
        )

        tij = round(rij)

        if tij < rij:
            dij = tij + 1
        else:
            dij = tij

        return dij

    def get_distance(self, city_a: int, city_b: int) -> int:
        return self.matrix[city_a][city_b]

    def print_info(self) -> None:

        print("=" * 50)
        print(f"Dataset: {self.name}")
        print(f"Liczba miast: {self.dimension}")
        print(f"Typ odległości: {self.edge_weight_type}")
        print(f"Rozmiar macierzy: "
              f"{self.dimension} x {self.dimension}")

    def print_sample(self, size: int = 5) -> None:

        print("\nFragment macierzy odległości:\n")

        for row in self.matrix[:size]:
            print(row[:size])
            