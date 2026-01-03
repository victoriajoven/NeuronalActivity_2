# src/jobmanager/jobshop_instance.py
class JobShopInstance:
    def __init__(self, jobs):
        """
        jobs: List[List[Tuple[machine_id, processing_time]]]
        """
        self.jobs = jobs
        self.num_jobs = len(jobs)
        self.num_machines = self._count_machines()

    def _count_machines(self):
        machines = set()
        for job in self.jobs:
            for machine, _ in job:
                machines.add(machine)
        return len(machines)
