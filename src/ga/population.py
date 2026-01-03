# src/ga/population.py
import random
from src.ga.chromosome import Chromosome
from src.evaluation.makespan import compute_makespan


class Population:
    """Population of chromosomes for the GA"""
    def __init__(self, chromosomes):
        self.chromosomes = chromosomes
        self.best_chromosome = None
        self.history_best_fitness = []

    @classmethod
    def initialize(cls, instance, size):
        base = []
        for job_id, job in enumerate(instance.jobs):
            base.extend([job_id] * len(job))

        chromosomes = []
        for _ in range(size):
            genes = base.copy()
            random.shuffle(genes)
            chromosomes.append(Chromosome(genes))

        return cls(chromosomes)

    def evaluate(self, instance):
        for c in self.chromosomes:
            if c.fitness is None:
                c.fitness = compute_makespan(c, instance)
        self._update_best()

    def _update_best(self):
        self.best_chromosome = min(self.chromosomes, key=lambda c: c.fitness)
        self.history_best_fitness.append(self.best_chromosome.fitness)

    def select_best(self, n):
        return sorted(self.chromosomes, key=lambda c: c.fitness)[:n]

    def replace(self, offspring, elitism=1):
        elites = self.select_best(elitism)
        self.chromosomes = elites + offspring[:len(self.chromosomes) - elitism]

    def is_converged(self, patience):
        if len(self.history_best_fitness) < patience:
            return False
        recent = self.history_best_fitness[-patience:]
        return all(f == recent[0] for f in recent)
