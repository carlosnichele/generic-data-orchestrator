import time
import logging

logger = logging.getLogger("retry")

def retry(times=3, delay=2):
    """
    Retry decorator with exponential backoff.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < times:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempt += 1
                    wait = delay * attempt
                    logger.warning(f"Error: {e}. Retrying in {wait}s...")
                    time.sleep(wait)
            raise Exception(f"Function '{func.__name__}' failed after {times} attempts.")
        return wrapper
    return decorator
