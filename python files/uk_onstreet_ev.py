import sys
from pathlib import Path
from typing import List

import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter


def main(argv: List[str] | None = None) -> int:
    # Data from the provided table (counts of on-street EV charging points)
    labels = [
        "ubitricity",
        "Char.gy",
        "SureCharge/FM Conway",
        "Connected Kerb",
        "Believ",
        "Trojan Energy Limited",
        "Blink Charging",
        "City EV",
        "ESB EV Solutions",
        "ChargePlace Scotland",
        "Swarco E.Connect",
        "ecars ESB",
        "Charge Your Car",
        "Wenea Services UK Limited",
        "eo Charging",
    ]
    values = [6764, 2911, 2460, 1842, 633, 463, 344, 181, 130, 106, 56, 47, 42, 35, 32]

    # Sort descending for a clear horizontal bar chart
    pairs = sorted(zip(values, labels), reverse=True)
    sorted_values, sorted_labels = zip(*pairs)

    fig, ax = plt.subplots(figsize=(9.5, 6.0))

    # Qualitative color palette for distinct bars
    palette = [
        "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
        "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf",
    ]
    colors = [palette[i % len(palette)] for i in range(len(sorted_labels))]

    bars = ax.barh(list(sorted_labels), list(sorted_values), color=colors)

    # Value labels on bars (thousands-separated)
    for bar, val in zip(bars, sorted_values):
        ax.text(
            bar.get_width() + max(sorted_values) * 0.01,
            bar.get_y() + bar.get_height() / 2,
            f"{val:,}",
            va="center",
            ha="left",
            fontsize=9,
            color="#222",
        )

    # Titles and axes formatting
    ax.set_title("UK On-street EV Charging Points by Network (Long Tail)")
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


