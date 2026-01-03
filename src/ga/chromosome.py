# src/ga/chromosome.py
from src.utils.logger import get_logger

logger = get_logger(__name__)

class Chromosome:
    """Chromosome representing a job sequence"""
    def __init__(self, genes):
        self.genes = genes
        self.fitness = None
        self.validate()

    def copy(self):
        c = Chromosome(self.genes.copy())
        c.fitness = self.fitness
        return c
    
    def validate(self, min_genes=2):
        """Check that the chromosome is valid for GA operators."""
        if self.genes is None:
            raise ValueError("Chromosome invalid: genes is None")
        if not isinstance(self.genes, (list, tuple)):
            raise ValueError(f"Chromosome invalid: genes must be list or tuple, got {type(self.genes)}")
        if len(self.genes) < min_genes:
            msg = f"Chromosome is invalid: has {len(self.genes)} genes, minimum required is {min_genes}"
            logger.error(msg)
            raise ValueError(f"Chromosome invalid: requires at least {min_genes} genes, got {len(self.genes)}")