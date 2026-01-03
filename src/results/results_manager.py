# src/results/results_manager.py
import json
import os
from datetime import datetime

RESULTS_DIR = "results/data"

def save_result(dataset_name, config_name, best_fitness, history):
    os.makedirs(RESULTS_DIR, exist_ok=True)
    
    result = {
        "dataset": dataset_name,
        "config": config_name,
        "best_fitness": best_fitness,
        "history": history,
        "timestamp": datetime.now().isoformat()
    }

    filename = f"{dataset_name}_{config_name}.json"
    path = os.path.join(RESULTS_DIR, filename)

    with open(path, "w") as f:
        json.dump(result, f, indent=2)

    return path