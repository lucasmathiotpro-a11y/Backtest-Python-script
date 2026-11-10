# EUR/USD Strategy Backtest (Python)

> **Status:** work in progress – last updated [11/10/2026]

## Overview
Independent project to design and backtest a quantitative trading strategy on the EUR/USD currency pair in Python. The goal is to apply a rigorous methodology (realistic assumptions, out-of-sample testing) rather than to claim a profitable strategy.

## Strategy
Trend-following strategy using a Simple Moving Average (SMA) crossover. Enters a long position when the fast SMA (20 periods) crosses above the slow SMA (50 periods) and exits when it crosses back below on daily EUR/USD data.

## Data
- **Pair:** EUR/USD
- **Period:** 2006 – 2021
- **Timeframe:** 4-Hour
- **Source:** OANDA

## Methodology
- **Libraries:** Python, Pandas, NumPy, Matplotlib
- **Assumptions:**
  - Spread: 1.5 pips fixed
  - Slippage: 0.5 pip per trade
  - Position sizing: 100% of available capital (no leverage)
- **Train / test split:**
  - In-sample (IS): 2006 – 2017 (development, calibration, and coverage of multiple market regimes)
  - Out-of-sample (OOS): 2018 – 2021 (unbiased performance evaluation)

## References
- Y. Hilpisch, *Financial Theory with Python: A Gentle Introduction*
- Y. Hilpisch, *Python for Algorithmic Trading: From Idea to Cloud Deployment*
- BlueFeverSoft YT channel, https://www.youtube.com/@BlueFeverSoft

## Disclaimer
Educational project only.
