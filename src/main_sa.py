# src/main_sa.py
from src.jobmanager.jobshop_instance import JobShopInstance
from src.jobmanager.parser import parse_orlib_jobshop
from src.optimizers.simulated_annealing import simulated_annealing
from src.ga.population import Population

def run_simmulated_annealing():    
    """ 
    Entry point for running Simulated Annealing on a JSSP instance. 
    """
    jobs = parse_orlib_jobshop("data/raw/ft06.txt")
    instance = JobShopInstance(jobs)


    population = Population.initialize(instance, size=50)
    population.evaluate(instance)
    initial_solution = population.best_chromosome.genes


    best_solution, best_fitness, history = simulated_annealing(
        initial_solution=initial_solution,
        instance=instance,
        initial_temperature=1000,
        final_temperature=1,
        alpha=0.95,
        max_iterations=2000
    )

    print("Best SA makespan:", best_fitness)


if __name__ == "__main__": 
    run_simmulated_annealing()
