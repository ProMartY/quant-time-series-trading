import pandas as pd

def moving_average_strategy(df, fast=3, slow=5):
    df = df.copy()

    df["fast_ma"] = df["close"].rolling(fast).mean()
    df["slow_ma"] = df["close"].rolling(slow).mean()

    df["signal"] = 0
    df.loc[df["fast_ma"] > df["slow_ma"], "signal"] = 1
    df.loc[df["fast_ma"] < df["slow_ma"], "signal"] = -1

    # shift signal to avoid look-ahead bias
    df["signal"] = df["signal"].shift(1)

    return df

