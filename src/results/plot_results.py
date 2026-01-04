# src/results/plot_results.py
import json
import os
import matplotlib.pyplot as plt

RESULTS_DIR = "results/data"
FIGURES_DIR = "results/plots"

def plot_fitness_evolution(result_path):
    """ 
    Plot fitness evolution from a single result file.
    """
    os.makedirs(FIGURES_DIR, exist_ok=True)

    with open(result_path) as f:
        result = json.load(f)

    history = result["history"]

    plt.figure()
    plt.plot(history, label=result["config"])
    plt.xlabel("Generation")
    plt.ylabel("Best makespan")
    plt.title(f"Fitness evolution - {result['dataset']}")
    plt.legend()
    plt.tight_layout()

    filename = os.path.basename(result_path).replace(".json", ".png")
    plt.savefig(os.path.join(FIGURES_DIR, filename))
    plt.close()

def plot_comparative(dataset_name):
    """
    Plot comparative fitness evolution for all configurations
    of the same dataset.
    """
    os.makedirs(FIGURES_DIR, exist_ok=True)

    results = []

    for file in os.listdir(RESULTS_DIR):
        if file.endswith(".json"):
            path = os.path.join(RESULTS_DIR, file)
            with open(path) as f:
                result = json.load(f)

            if result["dataset"] == dataset_name:
                results.append(result)

    if len(results) < 2:
        print(f"Not enough results to compare for {dataset_name}")
        return

    plt.figure()

    for result in results:
        plt.plot(
            result["history"],
            label=result["config"]
        )

    plt.xlabel("Generation")
    plt.ylabel("Best makespan")
    plt.title(f"Comparative fitness evolution - {dataset_name}")
    plt.legend()
    plt.tight_layout()

    filename = f"comparison_{dataset_name}.png"
    plt.savefig(os.path.join(FIGURES_DIR, filename))
    plt.close()
