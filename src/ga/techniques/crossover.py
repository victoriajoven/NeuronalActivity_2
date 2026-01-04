# src/ga/techniques/crossover.py
import random
from src.ga.chromosome import Chromosome


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
    
class JobBasedCrossover:
    """
    Job-Based Crossover (JBX).
    Randomly selects a subset of jobs from parent 1
    and preserves their positions; remaining genes are
    filled from parent 2.
    """

    def apply(self, parents):
        offspring = []

        for i in range(0, len(parents) - 1, 2):
            p1 = parents[i].genes
            p2 = parents[i + 1].genes

            jobs = list(set(p1))
            selected_jobs = set(
                random.sample(jobs, random.randint(1, len(jobs) - 1))
            )

            child = [None] * len(p1)

            # Copy selected jobs from parent 1
            for idx, gene in enumerate(p1):
                if gene in selected_jobs:
                    child[idx] = gene

            # Fill remaining positions from parent 2
            p2_iter = iter(p2)
            for idx in range(len(child)):
                if child[idx] is None:
                    while True:
                        g = next(p2_iter)
                        if child.count(g) < p1.count(g):
                            child[idx] = g
                            break

            offspring.append(Chromosome(child))

        return offspring

