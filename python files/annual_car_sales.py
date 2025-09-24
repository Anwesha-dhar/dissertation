import matplotlib.pyplot as plt
from pathlib import Path

# Data from your screenshot
avg_2010_2019 = 71.10
years_hist = [2019, 2020, 2021, 2022, 2023, 2024]
values_hist = [74.90, 63.80, 66.70, 67.30, 75.30, 78.00]

years_fcst = [2025, 2026]
values_fcst = [79.20, 80.00]

fig, ax = plt.subplots(figsize=(8.5, 5.0))

# Historical series
ax.plot(years_hist, values_hist, color="#1f77b4", linewidth=2.5, marker="o", label="Historical")

# Forecast series (dashed)
ax.plot(years_fcst, values_fcst, color="#ff7f0e", linewidth=2.5, marker="D", linestyle="--", label="Forecast")

# Connect last historical to first forecast to keep the curve continuous (optional)
ax.plot([years_hist[-1], years_fcst[0]], [values_hist[-1], values_fcst[0]],
        color="#ff7f0e", linewidth=2.0, linestyle="--")

# Shade the forecast region
ax.axvspan(min(years_fcst) - 0.5, max(years_fcst) + 0.5, color="#ff7f0e", alpha=0.08)

# Add 2010–2019 average as a reference line
ax.axhline(avg_2010_2019, color="#555", linestyle=":", linewidth=2, label="2010–2019 average")
ax.text(years_hist[0], avg_2010_2019 + 0.4, "2010–2019 avg: 71.1", color="#555")

# Labels and formatting
ax.set_title("Car Sales (Historical vs Forecast)")
ax.set_xlabel("Year")
ax.set_ylabel("Units (millions)")
ax.set_xlim(min(years_hist) - 0.5, max(years_fcst) + 0.5)
ax.grid(True, axis="y", linestyle=":", alpha=0.5)
ax.legend()

plt.tight_layout()

# Show window only; no file saving
plt.show()