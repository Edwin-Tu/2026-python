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

    output = Path(output_path)

    if output.parent != Path("."):
        output.parent.mkdir(parents=True, exist_ok=True)

    plt.figure()

    for algorithm_name, size_results in results.items():
        if not size_results:
            continue

        sizes = sorted(int(size) for size in size_results.keys())
        elapsed_times = [
            size_results[str(size)]
            for size in sizes
        ]

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


def main(input_path="results.json", output_path="assets/benchmark.png") -> None:
    results = load_results(input_path)
    plot_results(results, output_path)


if __name__ == "__main__":
    main()