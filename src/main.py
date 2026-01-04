# src/main.py
from src.experiments.runner import run_all_experiments

if __name__ == "__main__":
    """
    Main entry point to run all GA experiments on JSSP instances
    with different configurations and datasets.
    """
    run_all_experiments()