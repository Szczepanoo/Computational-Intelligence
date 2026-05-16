import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go


def plot_convergence(ae_history, de_history, function_name):

    ae_best = [
        h["best"]
        for h in ae_history
    ]

    de_best = [
        h["best"]
        for h in de_history
    ]

    plt.figure(figsize=(10, 6))

    plt.plot(ae_best, label="AE")
    plt.plot(de_best, label="DE")

    plt.xlabel("Generation")
    plt.ylabel("Best fitness")

    plt.title(
        f"Convergence - {function_name}"
    )

    plt.legend()

    plt.grid(True)

    plt.show()


def plot_population_3d(func, population, bounds):

    x = np.linspace(bounds[0], bounds[1], 100)
    y = np.linspace(bounds[0], bounds[1], 100)

    X, Y = np.meshgrid(x, y)

    Z = np.array([
        [
            func(np.array([x1, x2]))
            for x1 in x
        ]
        for x2 in y
    ])

    pop_x = population[:, 0]
    pop_y = population[:, 1]

    pop_z = np.array([
        func(np.array([x1, x2]))
        for x1, x2 in zip(pop_x, pop_y)
    ])

    fig = go.Figure()

    fig.add_trace(
        go.Surface(
            x=X,
            y=Y,
            z=Z,
            opacity=0.7
        )
    )

    fig.add_trace(
        go.Scatter3d(
            x=pop_x.tolist(),
            y=pop_y.tolist(),
            z=pop_z.tolist(),
            mode="markers",
            marker=dict(size=4)
        )
    )

    fig.show()
    

def visualize_population_steps(func, history, bounds):

    x = np.linspace(bounds[0], bounds[1], 100)
    y = np.linspace(bounds[0], bounds[1], 100)

    X, Y = np.meshgrid(x, y)

    Z = np.array([
        [
            func(np.array([x1, x2]))
            for x1 in x
        ]
        for x2 in y
    ])

    fig = go.Figure()

    fig.add_trace(
        go.Surface(
            x=X,
            y=Y,
            z=Z,
            opacity=0.7,
            showscale=False
        )
    )

    for i, step in enumerate(history):

        population = step["population"]

        pop_x = population[:, 0]
        pop_y = population[:, 1]

        pop_z = np.array([
            func(np.array([x1, x2]))
            for x1, x2 in zip(pop_x, pop_y)
        ])

        visible = (i == 0)

        fig.add_trace(
            go.Scatter3d(
                x=pop_x.tolist(),
                y=pop_y.tolist(),
                z=pop_z.tolist(),
                mode="markers",
                marker=dict(size=5),
                visible=visible,
                name=f"Generation {i}"
            )
        )

    steps = []

    for i in range(len(history)):

        visible = [True] + [False] * len(history)

        visible[i + 1] = True

        step = dict(
            method="update",
            args=[
                {
                    "visible": visible
                },
                {
                    "title": f"Generation {i}"
                }
            ],
            label=str(i)
        )

        steps.append(step)

    sliders = [dict(
        active=0,
        currentvalue={"prefix": "Generation: "},
        steps=steps
    )]

    fig.update_layout(
        sliders=sliders,
        scene=dict(
            xaxis_title="X1",
            yaxis_title="X2",
            zaxis_title="Fitness"
        )
    )

    fig.show()