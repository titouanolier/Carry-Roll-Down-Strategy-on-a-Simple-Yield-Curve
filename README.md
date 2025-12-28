# Carry-Roll-Down-Strategy-on-a-Simple-Yield-Curve
This project builds a simple bond strategy that exploits the US Treasury yield curve. The goal is to identify, each month, the maturity offering the highest expected return by combining:

- Carry: the yield of a bond if the yield curve remains unchanged.
- Roll-down: the gain (or loss) when a bond “rolls down” the curve as it approaches a shorter maturity on a sloped or inverted curve.

The strategy selects the optimal maturity each month and tracks performance over the following month. The project includes:

- Importing monthly US Treasury yields (2Y, 5Y, 10Y).
- Calculating carry and roll-down for each maturity.
- Selecting the most attractive maturity at each date.
- Backtesting the strategy and calculating cumulative returns, Sharpe ratio, and volatility.
- Visualizing performance and interpreting results.

Learning objectives:

- Understand the term structure of interest rates and its impact on bond returns.
- Apply fixed income concepts in an intuitive, quantitative way.
- Build a small, robust, and interpretable backtest in Python.
