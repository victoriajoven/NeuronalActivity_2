# src/experiments/runner.py
from src.jobmanager.parser import parse_orlib_jobshop
from src.jobmanager.jobshop_instance import JobShopInstance
from src.experiments.experiment import Experiment
from src.ga.techniques.selection import RouletteWheelSelection, TournamentSelection
from src.ga.techniques.crossover import JobBasedCrossover, PrecedencePreservingCrossover
from src.ga.techniques.mutation import InsertionMutation, InsertionMutation, SwapMutation
from src.results.plot_results import plot_comparative, plot_fitness_evolution
from src.results.results_manager import save_result


def run_all_experiments():
    """
    Run experiments for multiple datasets and configurations
    Datasets with different GA configurations (from ..OR-Library http://people.brunel.ac.uk/~mastjjb/jeb/orlib/files/jobshop1.txt)
    - SMALL: ft06.txt (6 jobs, 6 machines)
    - MEDIUM: la19.txt (10 jobs, 10 machines)
    - LARGE: yn1.txt (20 jobs, 20 machines)
    Store results and generate plots
    """
    datasets = {
        "SMALL 6x6 (ft06)": "data/raw/ft06.txt",
        "MEDIUM 10x10 (la19)": "data/raw/la19.txt",
        "LARGE 20x20 (yn1)": "data/raw/yn1.txt",
    }

    configs = [
    # Tournament + PPX + Swap
    {
        "name": "T_PPX_Swap",
        "population_size": 50,
        "selection": TournamentSelection(),
        "crossover": PrecedencePreservingCrossover(),
        "mutation": SwapMutation(0.1),
        "elitism": 1,
        "max_generations": 300,
        "patience": 30,
    },

    # Tournament + PPX + Insertion
    {
        "name": "T_PPX_Insert",
        "population_size": 50,
        "selection": TournamentSelection(),
        "crossover": PrecedencePreservingCrossover(),
        "mutation": InsertionMutation(0.1),
        "elitism": 1,
        "max_generations": 300,
        "patience": 30,
    },

    # Tournament + JBX + Swap
    {
        "name": "T_JBX_Swap",
        "population_size": 50,
        "selection": TournamentSelection(),
        "crossover": JobBasedCrossover(),
        "mutation": SwapMutation(0.1),
        "elitism": 1,
        "max_generations": 300,
        "patience": 30,
    },

    # Roulette + PPX + Swap
    {
        "name": "R_PPX_Swap",
        "population_size": 50,
        "selection": RouletteWheelSelection(),
        "crossover": PrecedencePreservingCrossover(),
        "mutation": SwapMutation(0.1),
        "elitism": 1,
        "max_generations": 300,
        "patience": 30,
    },

    # Roulette + JBX + Insertion
    {
        "name": "R_JBX_Insert",
        "population_size": 50,
        "selection": RouletteWheelSelection(),
        "crossover": JobBasedCrossover(),
        "mutation": InsertionMutation(0.1),
        "elitism": 1,
        "max_generations": 300,
        "patience": 30,
    },

    # Roulette + PPX + Insertion
    {
        "name": "R_PPX_Insert",
        "population_size": 50,
        "selection": RouletteWheelSelection(),
        "crossover": PrecedencePreservingCrossover(),
        "mutation": InsertionMutation(0.1),
        "elitism": 1,
        "max_generations": 300,
        "patience": 30,
    },
    ]


    for name, path in datasets.items():
        jobs = parse_orlib_jobshop(path)
        instance = JobShopInstance(jobs)

        for i, config in enumerate(configs):
            print(f"\n***** RUNNING INSTANCE {name} *****")
            print(f"Configuration: {config['name']}")
            experiment = Experiment(instance, config)
            best, history = experiment.run()
            print(f"Best makespan: {best.fitness}")
            
            result_path = save_result(
                dataset_name=name,
                config_name=config["name"],
                best_fitness=best.fitness,
                history=history
            )
            
            plot_fitness_evolution(result_path)
            
        # Comparative figure for this dataset
        plot_comparative(name)