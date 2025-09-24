import sys
from pathlib import Path
from typing import List

import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter


def main(argv: List[str] | None = None) -> int:
    # Data from the provided table (counts of on-street EV charging points)
    labels = [
        "Shell Recharge Ubitricity",
        "Connected Kerb",
        "Pod Point",
        "BP Pulse",
        "char.gy",
        "ChargePlace Scotland",
        "Source London",
        "SureCharge",
        "blink",
        "InstaVolt",
    ]
    values = [8984, 5865, 5043, 4141, 3503, 2830, 2638, 2555, 2165, 1835]

    # Sort descending by value for a clean horizontal bar chart
    pairs = sorted(zip(values, labels), reverse=True)
    sorted_values, sorted_labels = zip(*pairs)

    fig, ax = plt.subplots(figsize=(9, 5.5))

    # Choose a readable qualitative palette
    palette = [
        "#1f77b4",
        "#ff7f0e",
        "#2ca02c",
        "#d62728",
        "#9467bd",
        "#8c564b",
        "#e377c2",
        "#7f7f7f",
        "#bcbd22",
        "#17becf",
    ]
    colors = [palette[i % len(palette)] for i in range(len(sorted_labels))]

    bars = ax.barh(list(sorted_labels), list(sorted_values), color=colors)

    # Add value labels to the right of each bar with thousands separator
    for bar, val in zip(bars, sorted_values):
        ax.text(
            bar.get_width() + max(sorted_values) * 0.01,
            bar.get_y() + bar.get_height() / 2,
            f"{val:,}",
            va="center",
            ha="left",
            fontsize=10,
            color="#222",
        )

    # Titles and formatting
    ax.set_title("UK On-street EV Charging Points by Network (2024)")
    ax.set_xlabel("Number of charge points")
    ax.set_ylabel("")
    ax.xaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))
    ax.grid(axis="x", linestyle=":", alpha=0.5)
    ax.set_xlim(0, max(sorted_values) * 1.20)

    plt.tight_layout()

    # Show window
    plt.show()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())


