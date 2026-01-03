import json
import os
import matplotlib.pyplot as plt

RESULTS_DIR = "results/data"
FIGURES_DIR = "results/plots"

def plot_fitness_evolution(result_path):
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
