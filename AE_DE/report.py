import os
import pandas as pd


def create_results_directories():

    directories = ["results", "results/ae", "results/de"]

    for directory in directories:
        os.makedirs(directory, exist_ok=True)


def save_history_to_csv(history, filename):
    rows = []

    for step in history:

        rows.append({
            "generation": step["generation"],
            "best": step["best"],
            "mean": step["mean"],
            "worst": step["worst"]
            })

    df = pd.DataFrame(rows)

    df.to_csv(filename, index=False)

    print(f"Saved history to: {filename}")


def save_summary(summary_rows, filename):
    df = pd.DataFrame(summary_rows)

    df.to_csv(filename, index=False)

    print(f"Saved summary to: {filename}")


def generate_reports(function_name, ae_result, de_result, summary_rows):

    create_results_directories()

    save_history_to_csv(
        ae_result["history"],
        f"results/ae/{function_name}_ae.csv"
    )

    save_history_to_csv(
        de_result["history"],
        f"results/de/{function_name}_de.csv"
    )

    summary_rows.append({
        "function": function_name,
        "AE_best_fitness": ae_result["best_fitness"],
        "DE_best_fitness":de_result["best_fitness"]
        })


def finalize_summary(summary_rows):
    save_summary(summary_rows,"results/summary.csv")