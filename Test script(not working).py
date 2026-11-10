import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(42)
dates = pd.date_range(start="2006-01-01", end="2021-12-31", freq="4h")
prices = 1.20 + np.cumsum(np.random.normal(0, 0.001, len(dates)))
df = pd.DataFrame({"Close": prices}, index=dates)

# A
fast_window = 20
slow_window = 50

# B
df["SMA_Fast"] = df["Close"].rolling(window=fast_window).mean()
df["SMA_Slow"] = df["Close"].rolling(window=slow_window).mean()

# C
df["Signal"] = 0
df.loc[df["SMA_Fast"] > df["SMA_Slow"], "Signal"] = 1

# D
df["Position"] = df["Signal"].shift(1)

# E
df["Market_Return"] = df["Close"].pct_change()
df["Strategy_Return"] = df["Market_Return"] * df["Position"]

# F
df["Cumulative_Market"] = (1 + df["Market_Return"].fillna(0)).cumprod()
df["Cumulative_Strategy"] = (1 + df["Strategy_Return"].fillna(0)).cumprod()

# G
os.makedirs("results", exist_ok=True)

plt.figure(figsize=(12, 6))
plt.plot(
    df.index,
    df["Cumulative_Strategy"],
    label="Stratégie SMA Crossover",
    color="royalblue",
)
plt.plot(
    df.index,
    df["Cumulative_Market"],
    label="Buy & Hold (Benchmark)",
    color="gray",
    alpha=0.6,
)
plt.title("Backtest EUR/USD (4H) — SMA Crossover")
plt.xlabel("Date")
plt.ylabel("Valeur du portefeuille (Base 1)")
plt.legend()
plt.grid(True)

plt.savefig("results/equity_curve.png", dpi=300, bbox_inches="tight")
plt.show()

print("Backtest exécuté avec succès. Graphique sauvegardé dans results/equity_curve.png")
