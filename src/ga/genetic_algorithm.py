# src/ga/genetic_algorithm.py
from src.ga.population import Population

class GeneticAlgorithm:
    """Genetic Algorithm implementation for Job Shop Scheduling"""
    def __init__(
        self,
        instance,
        population_size,
        selection,
        crossover,
        mutation,
        elitism=1,
        max_generations=300,
        patience=30
    ):
        self.instance = instance
        self.population_size = population_size
        self.selection = selection
        self.crossover = crossover
        self.mutation = mutation
        self.elitism = elitism
        self.max_generations = max_generations
        self.patience = patience
        self.best_fitness_history = []

    def run(self):
        population = Population.initialize(
            self.instance, self.population_size
        )

        for gen in range(self.max_generations):
            population.evaluate(self.instance)

            if population.is_converged(self.patience):
                print(f"Converged at generation {gen}")
                break

            parents = self.selection.select(population)
            offspring = self.crossover.apply(parents)
            self.mutation.apply(offspring)
            population.replace(offspring, elitism=self.elitism)

        population.evaluate(self.instance)
        return population.best_chromosome, population.history_best_fitness
