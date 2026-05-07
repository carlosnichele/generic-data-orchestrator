import logging
import time

logger = logging.getLogger("helpers")

def timer(func):
    """
    Decorator to measure execution time of ETL steps.
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        logger.info(f"Starting: {func.__name__}")
        result = func(*args, **kwargs)
        elapsed = round(time.time() - start, 3)
        logger.info(f"Completed: {func.__name__} in {elapsed}s")
        return result
    return wrapper
