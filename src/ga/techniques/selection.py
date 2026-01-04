# src/ga/techniques/selection.py
# Selection techniques for genetic algorithms
import random
import numpy as np

class TournamentSelection:
    """
    Tournament Selection:
    Picks parents for the next generation by holding "mini-competitions" among small, 
    random subsets (tournaments) of the population, 
    selecting the fittest individual from each group to move forward, 
    effectively balancing selection pressure and diversity by adjusting the tournament size (k)
    """
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
            parents.append(min(contenders, key=lambda c: c.fitness).copy())

        return parents
    
class RouletteWheelSelection:
    """
    Roulette Wheel:
    Selection technique used in evolutionary algorithms for selecting potentially 
    useful solutions for recombination (inspired on the concept of a roulette wheel in a casino).
    """
    def select(self, population):
        parents = []
        pop = population.chromosomes
        pop_size = len(pop)

        # Ensure even number of parents
        if pop_size % 2 != 0:
            pop_size -= 1

        # Fitness values (minimization problem)
        fitnesses = np.array([c.fitness for c in pop])

        # Lower fitness = higher probability
        max_fitness = fitnesses.max()
        adjusted_fitness = max_fitness - fitnesses + 1e-6

        probabilities = adjusted_fitness / adjusted_fitness.sum()

        for _ in range(pop_size):
            selected = np.random.choice(pop, p=probabilities)
            parents.append(selected)

        return parents