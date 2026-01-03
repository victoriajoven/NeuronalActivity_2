import random
from ga.chromosome import Chromosome


class PrecedencePreservingCrossover:
    """
    Standard PPX for Job Shop Scheduling.
    Preserves operation counts and job precedences.
    """

    def apply(self, parents):
        offspring = []

        for i in range(0, len(parents) - 1, 2):
            p1 = parents[i].genes
            p2 = parents[i + 1].genes

            child = []
            r1 = p1.copy()
            r2 = p2.copy()

            while r1:
                if random.random() < 0.5:
                    gene = r1.pop(0)
                    r2.remove(gene)
                else:
                    gene = r2.pop(0)
                    r1.remove(gene)
                child.append(gene)

            offspring.append(Chromosome(child))

        return offspring