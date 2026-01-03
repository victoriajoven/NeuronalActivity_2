# src/evaluation/makespan.py

def compute_makespan(chromosome, instance):
    """Compute the makespan of a given chromosome on the job shop instance."""
    if instance.num_jobs == 0:
        return 0   
    
    machine_time = [0] * instance.num_machines
    job_time = [0] * instance.num_jobs
    job_op_index = [0] * instance.num_jobs

    for job_id in chromosome.genes:
        op_idx = job_op_index[job_id]
        machine, duration = instance.jobs[job_id][op_idx]

        start = max(machine_time[machine], job_time[job_id])
        end = start + duration

        machine_time[machine] = end
        job_time[job_id] = end
        job_op_index[job_id] += 1
        
    return max(job_time)
