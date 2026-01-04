# src/ga/techniques/mutation.py
import random

class SwapMutation:
    """
    Swap Mutation: 
    Swap two random genes in the chromosome.
    """

    def __init__(self, probability=0.1):
        self.probability = probability

    def apply(self, offspring):
        for c in offspring:
            if random.random() < self.probability:
                i, j = random.sample(range(len(c.genes)), 2)
                c.genes[i], c.genes[j] = c.genes[j], c.genes[i]
                c.fitness = None
                
class InsertionMutation:
    """
    Insertion Mutation: 
    Remove one gene and insert it in another random position.
    """

    def __init__(self, probability=0.1):
        self.probability = probability

    def apply(self, offspring):
        for c in offspring:
            if random.random() < self.probability:
                i, j = random.sample(range(len(c.genes)), 2)
                gene = c.genes.pop(i)
                c.genes.insert(j, gene)
                c.fitness = None