"""Benchmark Stage 2 sorting algorithms."""

import json
from random import Random
from time import perf_counter

from sorts import bubble_sort, merge_sort, quick_sort


SORT_FUNCTIONS = [bubble_sort, quick_sort, merge_sort]


def make_data(n: int, seed: int = 42) -> list:
    rng = Random(seed)
    return [rng.randint(-n, n) for _ in range(n)]


def run_benchmark(sizes=(500, 1000, 2000, 4000), repeats=3) -> dict:
    results = {
        "sizes": list(sizes),
        "repeats": repeats,
        "algorithms": {sort_func.__name__: {} for sort_func in SORT_FUNCTIONS},
    }

    for size in sizes:
        data = make_data(size)
        for sort_func in SORT_FUNCTIONS:
            records = []
            for _ in range(repeats):
                start = perf_counter()
                sort_func(data)
                records.append(perf_counter() - start)
            results["algorithms"][sort_func.__name__][str(size)] = {
                "records": records,
                "average": sum(records) / len(records),
            }

    return results


def print_table(results: dict) -> None:
    sizes = results["sizes"]
    algorithms = results["algorithms"]
    header = ["algorithm", *[str(size) for size in sizes]]
    rows = []

    for name, timings in algorithms.items():
        row = [name]
        for size in sizes:
            row.append(f"{timings[str(size)]['average']:.6f}")
        rows.append(row)

    widths = [
        max(len(row[index]) for row in [header, *rows])
        for index in range(len(header))
    ]
    print("  ".join(value.rjust(widths[index]) for index, value in enumerate(header)))
    for row in rows:
        print("  ".join(value.rjust(widths[index]) for index, value in enumerate(row)))


def main() -> None:
    results = run_benchmark()
    print_table(results)
    with open("results.json", "w", encoding="utf-8") as file:
        json.dump(results, file, indent=2)


if __name__ == "__main__":
    main()
