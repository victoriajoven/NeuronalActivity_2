# Parser for OR-Library job shop instances
import logging

def parse_orlib_jobshop(path):
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
