"""
logger.py
---------
Reusable logging utility.
"""

import logging

def setup_logger(name="nacirfa_logger", log_file="nacirfa.log", level=logging.INFO):
    handler = logging.FileHandler(log_file)
    console = logging.StreamHandler()

    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    handler.setFormatter(formatter)
    console.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    logger.addHandler(console)
    return logger

# Example usage:
if __name__ == "__main__":
    log = setup_logger()
    log.info("Logger initialized successfully.")

