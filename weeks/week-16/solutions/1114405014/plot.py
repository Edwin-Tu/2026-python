import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt


def load_results(input_path="results.json") -> dict:
    path = Path(input_path)

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def plot_results(results: dict, output_path="assets/benchmark.png") -> None:
    if not results:
        raise ValueError("results must not be empty")

    validated_series = _validate_and_collect_series(results)

    output = Path(output_path)

    if output.parent != Path("."):
        output.parent.mkdir(parents=True, exist_ok=True)

    plt.figure()

    for algorithm_name, sizes, elapsed_times in validated_series:
        plt.plot(
            sizes,
            elapsed_times,
            marker="o",
            label=algorithm_name,
        )

    plt.xlabel("Input size")
    plt.ylabel("Elapsed time (seconds)")
    plt.title("Sorting Benchmark")
    plt.yscale("log")
    plt.legend()
    plt.grid(True, which="both")
    plt.tight_layout()

    plt.savefig(output)
    plt.close()


def _validate_and_collect_series(results: dict) -> list:
    validated_series = []

    for algorithm_name, size_results in results.items():
        if not isinstance(size_results, dict):
            raise ValueError("each algorithm result must be a dict")

        if not size_results:
            continue

        sizes = []
        elapsed_times = []

        for size_text, elapsed in size_results.items():
            try:
                size = int(size_text)
            except ValueError as error:
                raise ValueError("size keys must be numeric") from error

            if size < 0:
                raise ValueError("size must be >= 0")

            if not isinstance(elapsed, (int, float)):
                raise ValueError("elapsed time must be numeric")

            if elapsed <= 0:
                raise ValueError("elapsed time must be > 0 for log scale")

            sizes.append(size)
            elapsed_times.append(float(elapsed))

        combined = sorted(zip(sizes, elapsed_times))
        sorted_sizes = [size for size, _ in combined]
        sorted_elapsed_times = [elapsed for _, elapsed in combined]

        validated_series.append(
            (algorithm_name, sorted_sizes, sorted_elapsed_times)
        )

    if not validated_series:
        raise ValueError("results must contain at least one data point")

    return validated_series


def main(input_path="results.json", output_path="assets/benchmark.png") -> None:
    results = load_results(input_path)
    plot_results(results, output_path)


if __name__ == "__main__":
    main()