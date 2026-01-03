# src/experiments/experiment.py
from ga.genetic_algorithm import GeneticAlgorithm
from utils.logger import get_logger

logger = get_logger(__name__)
class Experiment:
    """Class to run a GA experiment on a Job Shop Scheduling instance"""
    def __init__(self, instance, config):
        self.instance = instance
        self.config = config

    def run(self):
        logger.info(f"Starting experiment with configuration: {self.config}")
        ga = GeneticAlgorithm(
            instance=self.instance,
            population_size=self.config["population_size"],
            selection=self.config["selection"],
            crossover=self.config["crossover"],
            mutation=self.config["mutation"],
            elitism=self.config["elitism"],
            max_generations=self.config["max_generations"],
            patience=self.config["patience"]
        )
        return ga.run()