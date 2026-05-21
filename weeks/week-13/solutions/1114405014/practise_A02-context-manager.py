import time
from contextlib import contextmanager
import io
import sys

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.time() - self.start
        print(f"Elapsed: {elapsed:.4f} seconds")
        return False

@contextmanager
def section(title):
    print(f"\n{'='*40}")
    print(f"  {title}")
    print(f"{'='*40}")
    yield
    print(f"{'─'*40}")

@contextmanager
def capture_output():
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()
    try:
        yield buffer
    finally:
        sys.stdout = old_stdout

def solve_parity(n):
    bits = bin(n)[2:]
    ones = bits.count('1')
    print(f"The parity of {bits} is {ones} (mod 2 is {ones % 2}).")
