"""Timing utilities for Stage 1."""

from functools import wraps
from time import perf_counter


def timeit(func):
    """Decorate a function and record each call's elapsed time in seconds."""
    records = []

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        elapsed = perf_counter() - start
        wrapper.last_elapsed = elapsed
        wrapper.records.append(elapsed)
        return result

    wrapper.records = records
    return wrapper
