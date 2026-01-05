def backtest(df, initial_balance=10000, commission=0.001):
    balance = initial_balance
    position = 0
    equity_curve = []

    for i in range(len(df)):
        price = df["close"].iloc[i]
        signal = df["signal"].iloc[i]

        if signal == 1 and position == 0:
            position = balance / price
            balance = 0
            position *= (1 - commission)

        elif signal == -1 and position > 0:
            balance = position * price
            balance *= (1 - commission)
            position = 0

        equity = balance + position * price
        equity_curve.append(equity)

    return equity_curve

