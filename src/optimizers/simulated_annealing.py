# src/sa/simulated_annealing.py
import random
import math
from copy import deepcopy
from src.ga.chromosome import Chromosome
from src.evaluation.makespan import compute_makespan


def generate_neighbor(chromosome: Chromosome):
    """
     Generates a neighbor solution by applying a simple swap mutation. 
     This simulates the mutation behavior used in the Genetic Algorithm. 
     Returns a new Chromosome instance. 
    """
    genes = deepcopy(chromosome.genes)

    # Simulate mutation to generate neighbor
    i, j = random.sample(range(len(genes)), 2)
    genes[i], genes[j] = genes[j], genes[i]
    new_genes = genes

    return Chromosome(new_genes)


def simulated_annealing(
    initial_solution,
    instance,
    initial_temperature=1000.0,
    final_temperature=1.0,
    alpha=0.95,
    max_iterations=2000
):
    """
    Simulated Annealing for Job Shop Scheduling using the same encoding and fitness
    as the Genetic Algorithm.
    """

    # Convert initial solution (list of genes) into Chromosome
    current = Chromosome(deepcopy(initial_solution))
    current_fitness = compute_makespan(current, instance)

    best = Chromosome(deepcopy(initial_solution))
    best_fitness = current_fitness

    temperature = initial_temperature
    history = [best_fitness]

    iteration = 0

    while temperature > final_temperature and iteration < max_iterations:
        neighbor = generate_neighbor(current)
        neighbor_fitness = compute_makespan(neighbor, instance)

        delta = neighbor_fitness - current_fitness 

        if delta < 0:
            accept = True
        else:
            probability = math.exp(-delta / temperature)
            accept = random.random() < probability

        if accept:
            current = neighbor
            current_fitness = neighbor_fitness

        if current_fitness < best_fitness:
            best = Chromosome(deepcopy(current.genes))
            best_fitness = current_fitness

        history.append(best_fitness)

        temperature *= alpha
        iteration += 1

    return best.genes, best_fitness, history
