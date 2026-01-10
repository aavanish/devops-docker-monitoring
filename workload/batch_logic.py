#This file simulates a batch processing or we could say analytics engine with structured logging (running on PYTHON).
import time
import random
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("simulation-service")

def run_simulation():
    logger.info("Simulation triggered")

    for i in range(1, 11):
        cpu = random.uniform(20, 80)
        memory = random.uniform(200, 600)

        logger.info(
            f"Iteration={i} | CPU_Load={cpu:.2f}% | Memory_Consumption={memory:.2f}MB"
        )
        time.sleep(2)

    logger.info("Simulation completed")
