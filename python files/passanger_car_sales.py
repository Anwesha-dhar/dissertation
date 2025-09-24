import sys
from pathlib import Path
from typing import List

import matplotlib.pyplot as plt


def main(argv: List[str] | None = None) -> int:
    # Data from the provided table (percent shares)
    labels = [
        "Petrol",
        "Electric",
        "Diesel",
        "Hybrid",
        "Alternative",
    ]
    values = [51.20, 29.47, 16.07, 3.26, 0.0]

    # Sort descending by value for a cleaner horizontal bar chart
    pairs = sorted(zip(values, labels), reverse=True)
    sorted_values, sorted_labels = zip(*pairs)

    fig, ax = plt.subplots(figsize=(8.5, 5.0))
    bars = ax.barh(list(sorted_labels), list(sorted_values), color=["#4e79a7", "#f28e2b", "#59a14f", "#e15759", "#76b7b2"]) 

    # Add percentage labels at the end of bars
    for bar, val in zip(bars, sorted_values):
        ax.text(
            bar.get_width() + max(sorted_values) * 0.01,
            bar.get_y() + bar.get_height() / 2,
            f"{val:.2f}%",
            va="center",
            ha="left",
            fontsize=9,
            color="#222",
        )

    ax.set_title("Passenger Car Sales by Fuel/Drive Type (Market Share, %)")
    ax.set_xlabel("Market Share (%)")
    ax.set_ylabel("")
    ax.set_xlim(0, max(sorted_values) * 1.20)
    ax.grid(axis="x", linestyle=":", alpha=0.5)

    plt.tight_layout()
    plt.show()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())


