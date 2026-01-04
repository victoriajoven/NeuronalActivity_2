# src/ga/genetic_algorithm.py
from src.ga.population import Population

class GeneticAlgorithm:
    """
    Genetic Algorithm implementation for the JSSP:
    - This class manages the overall genetic algorithm process.
    - The algorithm iteratively evolves the population in order to minimize
    the makespan of the scheduling solution.
    """
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
        """
        GA initialization:
        - instance: Job Shop problem definition
        - population_size: number of chromosomes in the population
        - selection: selection technique used to choose parents
        - crossover: crossover technique used to generate offspring
        - mutation: mutation technique applied to offspring
        - elitism: number of best individuals preserved between generations
        - max_generations: upper bound on the number of generations
        - patience: number of generations without improvement used to detect convergence
        """
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
                print(f"Converged at generation: {gen}")
                break

            parents = self.selection.select(population)
            offspring = self.crossover.apply(parents)
            self.mutation.apply(offspring)
            population.replace(offspring, elitism=self.elitism)

        population.evaluate(self.instance)
        return population.best_chromosome, population.history_best_fitness
