# src/ga/techniques/selection.py
# Selection techniques for genetic algorithms
import random
import numpy as np

class TournamentSelection:
    """Tournament selection for genetic algorithms."""
    def __init__(self, tournament_size=3):
        self.tournament_size = tournament_size

    def select(self, population):
        parents = []
        pop = population.chromosomes
        pop_size = len(pop)

        # Ensure even number of parents
        if pop_size % 2 != 0:
            pop_size -= 1

        # Tournament size cannot exceed population size
        k = min(self.tournament_size, len(pop))

        for _ in range(pop_size):
            contenders = random.sample(pop, k)
            parents.append(min(contenders, key=lambda c: c.fitness))

        return parents