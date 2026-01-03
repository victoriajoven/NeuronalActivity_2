# src/jobmanager/parser.py
import logging

def parse_orlib_jobshop(path):
    """
    Parse a job shop instance from an OR-Library formatted file (f.e. ft06.txt).
    Args:
        path (str): Path to the OR-Library job shop instance file.
    Returns:
        list: A list of jobs, where each job is a list of (machine, processing_time) tuples.
    """
    jobs = []
    with open(path) as f:
        for line in f:
            try:
                values = list(map(int, line.split()))
                job = [(values[i], values[i + 1]) for i in range(0, len(values), 2)]
                jobs.append(job)
            except Exception as e:
                message = f"File '{path}', line: '{line}', error: {e}"
                logging.error(message)
                print(message)
    return jobs
