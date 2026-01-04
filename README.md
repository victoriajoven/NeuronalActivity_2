# A2: Optimization with Genetic Algorithms

## Overview

This project implements a **Genetic Algorithm (GA)** to solve the **Job Shop Scheduling Problem (JSSP)** 

The objective is to minimize the **makespan**, defined as the total completion time of all jobs, by evolving a population of candidate schedules through selection, crossover, and mutation operators.

The implementation is modular, extensible, and designed to allow systematic experimentation with different genetic operators and parameter configurations.

---

## Problem Description

The Job Shop Scheduling Problem (JSSP) is a classical combinatorial optimization problem in which:

- A set of **jobs** must be processed on a set of **machines**.
- Each job consists of an ordered sequence of **operations**.
- Each operation must be processed on a specific machine for a fixed duration.
- A machine can process only one operation at a time.
- Operations cannot be preempted.

The goal is to find a schedule that minimizes the **makespan**.

---

## Genetic Algorithm Approach

The optimization is performed using a **Genetic Algorithm (GA)**, defined by the following components:

### Chromosome Representation
- A chromosome is represented as a sequence of job identifiers.
- Each occurrence of a job corresponds to its next pending operation.
- This representation implicitly enforces job operation precedence constraints.

### Fitness Function
- The fitness of a chromosome is computed as the **makespan** of the corresponding schedule.
- Lower fitness values represent better solutions.

### Selection Operators
- Tournament Selection
- Roulette Wheel Selection

### Crossover Operators
- Precedence Preserving Crossover (PPX)
- Job-Based Crossover (JBX)

### Mutation Operators
- Swap Mutation
- Insertion Mutation

### Evolutionary Process
- The algorithm evolves a population over multiple generations.
- Elitism is used to preserve the best solutions.
- The algorithm stops when a maximum number of generations is reached or when no improvement is observed for a fixed number of generations.

---

## Project Structure
```
src/
├── experiments/
│ ├── __init__.py
│ ├── experiment.py             # Instance of experiment
│ └── runner.py                 # Script to run all experiments
│
├── ga/
│ ├── __init__.py
│ ├── chromosome.py             # Chromosome of job sequence
│ ├── population.py             # Population of chromosome
│ ├── genetic_algorithm.py      # Genetic Algorithm implementation for Job Shop Scheduling
│ └── techniques/
│   ├── __init__.py
│   ├── selection.py            # Tournament and Roulette Wheel
│   ├── crossover.py            # PPX and JBX
│   └── mutation.py             # Swap and Insertion
│
├── evaluation/
│ ├── __init__.py
│ └── makespan.py
│
├── jobmanager/
│ ├── __init__.py
│ ├── parser.py
│ └── jobshop_instance.py       # Generate an instance of jobs with job and machine
│
├── results/
│ ├── __init__.py
│ ├── results_manager.py        # Save experiments results as JSON to plot
│ └── plot_results.py           # Plot results
│
├── __init__.py
└── main.py                     # Main method to launch experiments
```

---

## Datasets

The algorithm was evaluated on Job Shop Scheduling instances of increasing size:

- **Small instance**: 6 machines (data/raw/ft06.txt)
- **Medium instance**: 10 machines (data/raw/la19.txt)
- **Large instance**: 20 machines (data/raw/yn1.txt)

The datasets follow the standard JSSP format, where each job is defined as a sequence of `(machine, processing_time)` pairs.  
Datasets with different GA configurations are recoverd from OR-Library http://people.brunel.ac.uk/~mastjjb/jeb/orlib/files/jobshop1.txt

---

## Experimental Setup

At least **six different configurations** were evaluated by combining:

- Two selection operators (Tournament and Roulette Wheel)
- Two crossover operators (PPX and JBX)
- Two mutation operators (Swap and Insertion)

This experimental design allows analyzing the impact of different genetic operators on convergence speed and solution quality.

For each configuration and dataset:
- The evolution of the best fitness value was recorded.
- Individual and comparative fitness evolution plots were generated.

---

## Results and Visualization

The project automatically generates:

- **Fitness evolution plots** showing the best makespan per generation
- **Comparative plots** comparing multiple configurations on the same dataset

All results are saved in structured JSON format.  Plots are stored as image files for reports and conclusions.

---

## References

Job Shop Scheduling Problem:
 - https://en.wikipedia.org/wiki/Job-shop_scheduling
Google Job Shop Problem:
 - https://developers.google.com/optimization/scheduling/job_shop
Github examples:
 - https://github.com/Incalos/FJSP-With-Genetic-Algorithm
 - https://github.com/samy-barrech/Flexible-Job-Shop-Scheduling-Problem
 - https://github.com/Eason0227/Job-shop-scheduling-problem/blob/main/GA%20for%20JSSP.ipynb

The optimization method implemented in this project is based on Genetic Algorithms.

---

## Jupyter Notebook Base Example

Before creating the structure of the project in Python, a Jupyter notebook has been created based on the master's documentation, the document references and different GitHub repositories.  

Although it is not exactly the same as the content of the project, it facilitates the understanding of the optimization of the genetic algorithm applied to the Job Shop Problem.

The Jupyter notebook is ***GA_JSSP_Basic_example.ipynb*** (located on notebooks/ directory).


---

## How to Run

1. Create a virtual environment:
   ```bash
   python -m venv .venv

2. Activate the virtual environment:
   ```bash
   source .venv/bin/activate  # macOS / Linux
   .venv\Scripts\activate     # Windows

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt

4. Run the experiments:
   ```python
   python -m src.main

5. Results data and plots will be generated automatically in the ***results/*** directory.

## Author
Victoria Joven