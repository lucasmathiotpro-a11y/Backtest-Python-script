import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. Chargement des données (ex: fichier CSV exporté d'OANDA)
# Colonnes minimales attendues : Date, Close
# df = pd.read_csv('data/eurusd_4h.csv', parse_dates=True, index_col='Date')

# Simulation de données factices si tu n'as pas encore le CSV (à supprimer)
np.random.seed(42)
dates = pd.date_range(start="2006-01-01", end="2021-12-31", freq="4h")
prices = 1.20 + np.cumsum(np.random.normal(0, 0.001, len(dates)))
df = pd.DataFrame({"Close": prices}, index=dates)

# 2. Paramètres de la stratégie (SMA Crossover)
fast_window = 20
slow_window = 50

# Calcul des moyennes mobiles
df["SMA_Fast"] = df["Close"].rolling(window=fast_window).mean()
df["SMA_Slow"] = df["Close"].rolling(window=slow_window).mean()

# 3. Génération des signaux
# 1 si la SMA rapide est au-dessus de la lente, 0 sinon
df["Signal"] = 0
df.loc[df["SMA_Fast"] > df["SMA_Slow"], "Signal"] = 1

# Shift pour éviter le biais de anticipation (on entre au début de la bougie suivante)
df["Position"] = df["Signal"].shift(1)

# 4. Calcul des performances
df["Market_Return"] = df["Close"].pct_change()
df["Strategy_Return"] = df["Market_Return"] * df["Position"]

# Calcul des courbes cumulées
df["Cumulative_Market"] = (1 + df["Market_Return"].fillna(0)).cumprod()
df["Cumulative_Strategy"] = (1 + df["Strategy_Return"].fillna(0)).cumprod()

# 5. Sauvegarde du graphique dans results/
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