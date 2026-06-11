import json
import random
import time
from pathlib import Path

from sorts import bubble_sort, quick_sort, merge_sort, optimized_quick_sort


def make_data(n: int, seed: int = 42) -> list:
    if n < 0:
        raise ValueError("n must be >= 0")

    rng = random.Random(seed)
    return [rng.randint(-n, n) for _ in range(n)]


def run_benchmark(sizes=(500, 1000, 2000, 4000), repeats=3) -> dict:
    if repeats < 1:
        raise ValueError("repeats must be >= 1")

    algorithms = {
        "bubble_sort": bubble_sort,
        "quick_sort": quick_sort,
        "merge_sort": merge_sort,
        "sorted": sorted,
        "optimized_quick_sort": optimized_quick_sort,
    }

    results = {
        algorithm_name: {}
        for algorithm_name in algorithms
    }

    for size in sizes:
        if size < 0:
            raise ValueError("sizes must contain only values >= 0")

        for algorithm_name, sort_func in algorithms.items():
            total_elapsed = 0.0

            for repeat_index in range(repeats):
                data = make_data(size, seed=42 + repeat_index)

                start = time.perf_counter()
                sort_func(data)
                elapsed = time.perf_counter() - start

                total_elapsed += elapsed

            average_elapsed = total_elapsed / repeats
            results[algorithm_name][str(size)] = average_elapsed

    return results


def save_results(results: dict, output_path: str = "results.json") -> None:
    path = Path(output_path)

    if path.parent != Path("."):
        path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(results, file, indent=2)


def print_table(results: dict) -> None:
    sizes = _collect_sizes(results)

    header = ["algorithm"] + sizes
    rows = []

    for algorithm_name, size_results in results.items():
        row = [algorithm_name]

        for size in sizes:
            elapsed = size_results.get(size)

            if elapsed is None:
                row.append("-")
            else:
                row.append(f"{elapsed:.6f}")

        rows.append(row)

    widths = [
        max(len(str(row[index])) for row in [header] + rows)
        for index in range(len(header))
    ]

    print(_format_row(header, widths))
    print(_format_row(["-" * width for width in widths], widths))

    for row in rows:
        print(_format_row(row, widths))


def _collect_sizes(results: dict) -> list:
    sizes = set()

    for size_results in results.values():
        sizes.update(size_results.keys())

    return [str(size) for size in sorted(int(size) for size in sizes)]


def _format_row(row: list, widths: list) -> str:
    return " | ".join(
        str(value).ljust(width)
        for value, width in zip(row, widths)
    )


if __name__ == "__main__":
    benchmark_results = run_benchmark()
    save_results(benchmark_results, "results.json")
    print_table(benchmark_results)