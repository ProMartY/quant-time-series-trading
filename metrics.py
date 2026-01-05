import numpy as np

def max_drawdown(equity):
    equity = np.array(equity)
    peak = np.maximum.accumulate(equity)
    drawdown = (equity - peak) / peak
    return drawdown.min()

def sharpe_ratio(equity):
    returns = np.diff(equity) / equity[:-1]
    if returns.std() == 0:
        return 0
    return np.mean(returns) / np.std(returns) * np.sqrt(252)

