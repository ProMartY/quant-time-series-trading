import pandas as pd
import matplotlib.pyplot as plt

from strategy import moving_average_strategy
from backtest import backtest
from metrics import max_drawdown, sharpe_ratio

df = pd.read_csv("data/sample_data.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
df.set_index("timestamp", inplace=True)

df = moving_average_strategy(df)

equity = backtest(df)

print("Max Drawdown:", max_drawdown(equity))
print("Sharpe Ratio:", sharpe_ratio(equity))

plt.plot(equity)
plt.title("Equity Curve")
plt.show()

