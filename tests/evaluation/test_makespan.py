# tests/evaluation/test_makespan.py
# Expected makespans are previsously calculated
import pytest
from src.evaluation.makespan import compute_makespan

class FakeChromosome:
    def __init__(self, genes):
        self.genes = genes

class FakeInstance:
    def __init__(self, jobs, num_machines):
        self.jobs = jobs
        self.num_jobs = len(jobs)
        self.num_machines = num_machines

def test_compute_makespan_simple():
    # J0: (machine, duration)
    # J1: (machine, duration)
    jobs = [
        [(0, 3), (1, 2)],  # J0
        [(1, 4), (0, 1)],  # J1
    ]

    instance = FakeInstance(jobs=jobs, num_machines=2)

    # Ops order:
    chromosome = FakeChromosome(
        genes=[0, 1, 0, 1]
    )

    makespan = compute_makespan(chromosome, instance)

    assert makespan == 6    

def test_compute_makespan_single_job():
    jobs = [
        [(0, 2), (1, 3)]
    ]

    instance = FakeInstance(jobs, num_machines=2)
    chromosome = FakeChromosome([0, 0])

    makespan = compute_makespan(chromosome, instance)

    assert makespan == 5


def test_compute_makespan_empty():
    instance = FakeInstance([], num_machines=0)
    chromosome = FakeChromosome([])

    makespan = compute_makespan(chromosome, instance)

    assert makespan == 0
    
def test_invalid_chromosome_raises():
    jobs = [[(0, 1)]]
    instance = FakeInstance(jobs, num_machines=1)
    chromosome = FakeChromosome([0, 0])  # demasiadas ops

    with pytest.raises(ValueError):
        compute_makespan(chromosome, instance)
