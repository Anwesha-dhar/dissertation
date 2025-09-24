import sys
from pathlib import Path
from typing import List

import matplotlib.pyplot as plt
import numpy as np


def main(argv: List[str] | None = None) -> int:
    # Categories in order from most negative to most positive, with a neutral and Don't know
    categories = [
        "Strongly oppose",
        "Oppose",
        "Neither",
        "Support",
        "Strongly support",
        "Don't know",
    ]

    # Data from the table (percentages) for each question
    q_labels = [
        "New vehicles phase-out",
        "Second-hand vehicles exemption",
    ]
    q_values = np.array([
        [22, 22, 18, 20, 13, 4],   # row 1 mapped into the categories order above
        [20, 18, 18, 25, 14, 5],   # row 2
    ], dtype=float)

    # Normalize to ensure each row sums to 100 (guard against small rounding differences)
    row_sums = q_values.sum(axis=1, keepdims=True)
    q_values = q_values / row_sums * 100.0

    # Colors: negatives (reds), neutral (gray), positives (greens), don't know (light gray)
    colors = ["#d62728", "#ff9896", "#c7c7c7", "#98df8a", "#2ca02c", "#e7e7e7"]

    # We build a diverging 100% stacked horizontal bar chart, centered around the neutral category
    # Compute cumulative left positions
    lefts = np.zeros(q_values.shape[0])

    fig, ax = plt.subplots(figsize=(10.0, 3.8))

    for idx, (cat, color) in enumerate(zip(categories, colors)):
        vals = q_values[:, idx]
        bars = ax.barh(q_labels, vals, left=lefts, color=color, edgecolor="white", linewidth=0.5, label=cat)
        # Add labels for segments that are large enough
        for bar, val in zip(bars, vals):
            if val >= 6:  # avoid clutter on very small segments
                ax.text(
                    bar.get_x() + bar.get_width() / 2,
                    bar.get_y() + bar.get_height() / 2,
                    f"{val:.0f}%",
                    ha="center",
                    va="center",
                    fontsize=9,
                    color="#111",
                )
        lefts = lefts + vals

    # Reference lines every 20% (use valid color and alpha)
    for x in [20, 40, 60, 80]:
        ax.axvline(x, color="#000000", alpha=0.08)

    ax.set_xlim(0, 100)
    ax.set_xlabel("Share of respondents (%)")
    ax.set_ylabel("")
    ax.set_title("Public support for EV-related policies (share of respondents)")
    ax.legend(ncol=3, bbox_to_anchor=(0.5, -0.2), loc="upper center")
    ax.grid(False)

    # Emphasize 0-100 framing
    ax.set_xticks([0, 20, 40, 60, 80, 100])

    plt.tight_layout()

    # Show window
    plt.show()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())


