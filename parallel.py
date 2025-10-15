"""
Parallel processing example using concurrent.futures.

This module demonstrates parallel execution of counting functions
using Python's ProcessPoolExecutor for CPU-bound tasks.
"""

import concurrent.futures
import random
import time


def count_a() -> None:
    """
    Count from 1 to 100 with a delay between each number.
    
    This function simulates a CPU-intensive task by generating
    random numbers between iterations.
    """
    for i in range(1, 101):
        print(f"CountA: {i}")
        # Delay: generate meaningless random numbers
        for _ in range(100000):
            random.randint(1, 100)


def count_b() -> None:
    """
    Count from 100 down to 1 with a delay between each number.
    
    This function simulates a CPU-intensive task by generating
    random numbers between iterations.
    """
    for i in range(100, 0, -1):
        print(f"CountB: {i}")
        # Delay: generate meaningless random numbers
        for _ in range(100000):
            random.randint(1, 100)


def main() -> None:
    """
    Execute count_a and count_b in parallel using ProcessPoolExecutor.
    
    This demonstrates how multiple CPU-bound tasks can run simultaneously
    using separate processes.
    """
    print("Starte das Zählen")
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(count_a), executor.submit(count_b)]
        concurrent.futures.wait(futures)
    
    print("Zählen beendet.")


if __name__ == "__main__":
    main()
