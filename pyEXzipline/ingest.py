import pandas as pd
import pytz
from pyEX import chartDF


def _get_data(symbol, start, end):
    df = chartDF('aapl', '5y')
    df = df[['open', 'close', 'high', 'low', 'volume']].set_index(df['date'])
    df.index = pd.to_datetime(df.index)
    if start:
        df = df[df.index > start]
    if end:
        df = df[df.index < end]

    return df


def load_from_iex(symbols, start=None, end=None):
    data = {}
    for symbol in symbols:
        data[symbol] = _get_data(symbol, start, end)

    panel = pd.Panel(data)
    # panel.major_axis = panel.major_axis.tz_localize(pytz.utc)
    return panel
