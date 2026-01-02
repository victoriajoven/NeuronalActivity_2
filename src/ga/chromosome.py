# src/ga/chromosome.py

class Chromosome:
    """Chromosome representing a job sequence"""
    def __init__(self, genes):
        self.genes = genes
        self.fitness = None

    def copy(self):
        c = Chromosome(self.genes.copy())
        c.fitness = self.fitness
        return c