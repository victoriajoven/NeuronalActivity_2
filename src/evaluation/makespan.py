# src/evaluation/makespan.py
import logging

def compute_makespan(chromosome, instance):
    """Compute the makespan of a given chromosome on the job shop instance."""
    # Handle empty instance
    if instance.num_jobs == 0:
        return 0   
    
    machine_time = [0] * instance.num_machines
    job_time = [0] * instance.num_jobs
    job_op_index = [0] * instance.num_jobs

    for job_id in chromosome.genes:
        op_idx = job_op_index[job_id]
        
        # Validate operation index
        if op_idx >= len(instance.jobs[job_id]):
            logging.error(f"Chromosome has invalid operation index for job {job_id}: {op_idx}")
            raise ValueError(f"Invalid chromosome: job_id={job_id}, op_idx={op_idx}, "
                             f"only {len(instance.jobs[job_id])} operations")
        
        machine, duration = instance.jobs[job_id][op_idx]

        start = max(machine_time[machine], job_time[job_id])
        end = start + duration

        machine_time[machine] = end
        job_time[job_id] = end
        job_op_index[job_id] += 1
        
    return max(job_time)
