import time
import logging

logger = logging.getLogger("scheduler")

class Scheduler:
    """
    Simple scheduler that runs a pipeline once.
    Can be extended for cron-like behavior.
    """
    def run(self, pipeline_function):
        logger.info("Scheduler started")
        pipeline_function()
        logger.info("Scheduler finished")
