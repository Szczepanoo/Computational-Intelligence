from dataclasses import dataclass
from pathlib import Path


@dataclass
class TSPInstance:
    name: str
    dimension: int
    edge_weight_type: str
    coordinates: list[tuple[int, float, float]]


class TSPParser:

    @staticmethod
    def load(filepath: str | Path) -> TSPInstance:
        filepath = Path(filepath)

        if not filepath.exists():
            raise FileNotFoundError(f"Nie znaleziono pliku: {filepath}")

        name = ""
        dimension = 0
        edge_weight_type = ""
        coordinates = []

        in_coord_section = False

        with open(filepath, "r", encoding="utf-8") as file:
            for raw_line in file:
                line = raw_line.strip()

                if not line:
                    continue

                if line == "EOF":
                    break

                if line == "NODE_COORD_SECTION":
                    in_coord_section = True
                    continue

                if in_coord_section:
                    parts = line.split()

                    if len(parts) < 3:
                        continue

                    city_id = int(parts[0])
                    x = float(parts[1])
                    y = float(parts[2])

                    coordinates.append((city_id, x, y))
                    continue

                if ":" in line:
                    key, value = map(str.strip, line.split(":", 1))
                else:
                    parts = line.split(maxsplit=1)

                    if len(parts) != 2:
                        continue

                    key, value = parts

                key = key.upper()

                if key == "NAME":
                    name = value

                elif key == "DIMENSION":
                    dimension = int(value)

                elif key == "EDGE_WEIGHT_TYPE":
                    edge_weight_type = value

        if not coordinates:
            raise ValueError("Nie znaleziono współrzędnych miast.")

        if dimension != len(coordinates):
            raise ValueError(
                f"Niezgodna liczba miast. "
                f"DIMENSION={dimension}, "
                f"wczytano={len(coordinates)}"
            )

        return TSPInstance(
            name=name,
            dimension=dimension,
            edge_weight_type=edge_weight_type,
            coordinates=coordinates
        )


    @staticmethod
    def read_all(data_folder: str | Path = "data") -> list[TSPInstance]:
        data_folder = Path(data_folder)

        if not data_folder.exists():
            raise FileNotFoundError(f"Folder nie istnieje: {data_folder}")

        tsp_files = sorted(data_folder.glob("*.tsp"))

        if not tsp_files:
            raise ValueError(f"Nie znaleziono plików .tsp w folderze: {data_folder}")

        instances = []

        print("\nWczytywanie datasetów TSPLib:\n")

        for tsp_file in tsp_files:
            instance = TSPParser.load(tsp_file)
            instances.append(instance)

            print("=" * 50)
            print(f"Nazwa: {instance.name}")
            print(f"Liczba miast: {instance.dimension}")
            print(f"Typ odległości: {instance.edge_weight_type}")

        print("\nZakończono wczytywanie datasetów.\n")

        return instances
    