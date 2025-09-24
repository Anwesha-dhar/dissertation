import sys
from pathlib import Path
from typing import List

import matplotlib.pyplot as plt
import numpy as np


def main(argv: List[str] | None = None) -> int:
    # Years covered in the forecast
    years = list(range(2016, 2030))

    # Values taken from the provided image (revenue forecast by vehicle type)
    # Units are not specified in the image; label kept generic as "billion".
    plug_in_hybrid = np.array([
        1.10, 1.40, 1.70, 1.60, 2.80, 4.80, 5.40, 7.50,
        8.60, 8.70, 9.50, 10.40, 11.30, 12.30
    ], dtype=float)
    battery_electric = np.array([
        0.40, 0.60, 0.60, 1.40, 4.10, 6.80, 16.70, 19.30,
        23.00, 23.20, 25.20, 27.20, 29.30, 31.60
    ], dtype=float)

    fig, ax = plt.subplots(figsize=(9.5, 5.8))

    ax.plot(years, plug_in_hybrid, label="Plug-in hybrid electric vehicles", color="#4e79a7", marker="o")
    ax.plot(years, battery_electric, label="Battery-electric vehicles", color="#e15759", marker="s")

    # Formatting
    ax.set_xlabel("Year")
    ax.set_ylabel("Revenue (billion)")
    ax.set_xticks(years[::1])
    ax.set_xlim(min(years) - 0.2, max(years) + 0.2)
    ax.grid(True, axis="both", linestyle=":", alpha=0.5)
    ax.legend(loc="upper left")

    # Annotate last points for quick readability
    ax.annotate(f"{plug_in_hybrid[-1]:.1f}", xy=(years[-1], plug_in_hybrid[-1]), xytext=(5, 8),
                textcoords="offset points", color="#4e79a7")
    ax.annotate(f"{battery_electric[-1]:.1f}", xy=(years[-1], battery_electric[-1]), xytext=(5, -14),
                textcoords="offset points", color="#e15759")

    fig.suptitle("UK EV Revenue Forecast by Vehicle Type (2016–2029)")
    fig.tight_layout(rect=[0, 0, 1, 0.95])

    # Display only; no file saving as requested

    # Show window
    plt.show()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())


