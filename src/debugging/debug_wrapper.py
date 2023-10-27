#!/usr/bin/env python3
import logging
import os
import inspect
from src.settings.config import LOG_STEP_COUNTER, LOG_NAME, LOGGING_DIR

new_log_path = LOGGING_DIR + LOG_NAME
if os.path.exists(new_log_path):
    os.remove(new_log_path)
    
if not os.path.exists(LOGGING_DIR):
    os.makedirs(LOGGING_DIR)


echo_buffer = []

log_step_counter = LOG_STEP_COUNTER

file_handler = logging.FileHandler(new_log_path, mode='w')
file_handler.setFormatter(logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s'))
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.CRITICAL)
console_handler.setFormatter(logging.Formatter('%(message)s'))

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def echo_log(message):
    global echo_buffer
    echo_buffer.append(message)

def echo(func):
    def wrapper(*args, **kwargs):
        global log_step_counter, echo_buffer
        try:
            log_step_counter += 1

            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()

            arg_strs = []
            for k, v in bound_args.arguments.items():
                arg_strs.append(f"{k}={v}")

            func_info = f"{func.__name__}({', '.join(arg_strs)})"

            if echo_buffer:
                logged_output = ' '.join(echo_buffer)
                logger.debug(f"Step {log_step_counter}: {func_info} echoed: {logged_output.strip()}")
                echo_buffer.clear()
            else:
                logger.debug(f"Step {log_step_counter}: Entered {func_info}")

            logger.info(f"{log_step_counter}: {func.__name__}")

            result = func(*args, **kwargs)
            return result
        except Exception as e:
            logger.error(f"An error occurred in the echo wrapper: {e}")
            raise
    return wrapper




