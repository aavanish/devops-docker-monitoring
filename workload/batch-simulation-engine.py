#This file simulates a batch processing or we could say analytics engine with structured logging (running on PYTHON).
import time
import random
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(module)s | %(message)s"
)

class BatchSimulationEngine:

    def __init__(self, total_iterations=10):
        self.total_iterations = total_iterations

    def execute(self):
        logging.info("Batch Simulation Engine initialized")

        for iteration in range(1, self.total_iterations + 1):
            cpu_load = random.uniform(25, 85)
            memory_usage = random.uniform(150, 600)

            logging.info(
                f"Iteration={iteration} | CPU_Load={cpu_load:.2f}% | "
                f"Memory_Consumption={memory_usage:.2f}MB"
            )

            time.sleep(2)

        logging.info("Batch Simulation Engine completed successfully")


if __name__ == "__main__":
    engine = BatchSimulationEngine(total_iterations=10)
    engine.execute()

