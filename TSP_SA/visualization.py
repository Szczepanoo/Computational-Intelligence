from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from parser import TSPInstance


class Visualizer:

    def __init__(self, output_dir: str = "results"):

        self.output_dir = Path(output_dir)

        self.routes_dir = (self.output_dir / "routes")

        self.charts_dir = (self.output_dir / "charts")

        self.animations_dir = (self.output_dir / "animations")

        self.routes_dir.mkdir(parents=True, exist_ok=True)

        self.charts_dir.mkdir(parents=True, exist_ok=True)

        self.animations_dir.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def extract_coordinates(tsp: TSPInstance):

        x_coords = []
        y_coords = []

        for _, x, y in tsp.coordinates:

            x_coords.append(x)
            y_coords.append(y)

        return x_coords, y_coords

    def plot_route(self, tsp: TSPInstance, route: list[int], 
                   distance: float, title: str = "TSP Route", save: bool = True):

        x_coords, y_coords = self.extract_coordinates(tsp)

        route_x = [x_coords[i] for i in route]

        route_y = [y_coords[i] for i in route]

        route_x.append(route_x[0])
        route_y.append(route_y[0])

        plt.figure(figsize=(10, 10))

        plt.plot(route_x, route_y)

        plt.scatter(route_x, route_y, s=10)

        plt.title(f"{title}\n"
            f"Distance: {distance}")

        plt.xlabel("X")
        plt.ylabel("Y")

        plt.tight_layout()

        if save:

            filename = (self.routes_dir / f"{tsp.name}_route.png")

            plt.savefig(filename, dpi=300)

            print(f"\nZapisano trasę: "
                f"{filename}")

        plt.show()

    def plot_convergence(self, history, dataset_name: str, save: bool = True):

        plt.figure(figsize=(12, 6))

        plt.plot(history["iteration"], history["best_distance"])

        plt.xlabel("Iteration")
        plt.ylabel("Best Distance")

        plt.title(f"Convergence Plot - {dataset_name}")

        plt.grid(True)

        plt.tight_layout()

        if save:

            filename = (self.charts_dir / f"{dataset_name}_convergence.png")

            plt.savefig(filename, dpi=300)

            print(f"\nZapisano convergence plot: {filename}")

        plt.show()

    def plot_temperature(self, history, dataset_name: str, save: bool = True):

        plt.figure(figsize=(12, 6))

        plt.plot(history["iteration"], history["temperature"])

        plt.xlabel("Iteration")
        plt.ylabel("Temperature")

        plt.title(f"Temperature Schedule - {dataset_name}")

        plt.grid(True)

        plt.tight_layout()

        if save:

            filename = (self.charts_dir / f"{dataset_name}_temperature.png")

            plt.savefig(filename, dpi=300)

            print(f"\nZapisano temperature plot: {filename}")

        plt.show()

    def animate_route_evolution(self, tsp: TSPInstance, routes_history: list[list[int]], 
                                distances_history: list[float], interval: int = 100,save: bool = True):

        x_coords, y_coords = (self.extract_coordinates(tsp))

        fig, ax = plt.subplots(figsize=(10, 10))

        line, = ax.plot([], [])
        
        ax.scatter(x_coords, y_coords, s=10)

        ax.set_title(f"SA Route Evolution - {tsp.name}")

        def update(frame):

            route = routes_history[frame]

            route_x = [x_coords[i] for i in route]

            route_y = [y_coords[i] for i in route]

            # Domknięcie cyklu
            route_x.append(route_x[0])
            route_y.append(route_y[0])

            line.set_data(route_x, route_y)

            ax.set_title(f"{tsp.name} | Step: {frame} | Distance: {distances_history[frame]}")

            return line,

        animation = FuncAnimation(fig, update, frames=len(routes_history), interval=interval, blit=False)

        if save:

            filename = self.animations_dir/ f"{tsp.name}_animation.gif"

            def progress_callback(current_frame, total_frames_count):

                percent = ((current_frame + 1) / total_frames_count) * 100

                print(f"\rGenerowanie animacji: {current_frame + 1}/{total_frames_count} ({percent:.1f}%)", end="")

            animation.save(filename, writer="pillow", progress_callback=progress_callback)

            print("\nAnimacja zapisana.")

            print(f"\nZapisano animację: {filename}")

        plt.show()

