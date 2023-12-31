import pandas as pd
import yfinance as yf
import datetime as dt
import argparse

interval_options = {
    "1m": 60, 
    "15m": 900,
    "": 24*60*60
}

def get_stock(symbol:str, start_datetime: dt.datetime, end_datetime:dt.datetime, interval:str = ""):
    """
    
    """
    symbol = symbol.upper()
    if interval not in interval_options.keys():
        raise Exception(f"No interval symbol: {interval}")

    if interval:
        data = yf.download(symbol, start_datetime, end_datetime, interval=interval)
    else:
        data = yf.download(symbol, start_datetime, end_datetime)

    data_tz = data.tz_localize(yf.Ticker(symbol).info['timeZoneFullName'])
    d = data_tz.reset_index()

    if 'Date' in d.columns:
        d['observed_at'] = d.Date.apply(lambda x: x+dt.timedelta(hours=23,minutes=59))
    elif 'Datetime' in d.columns:
        d['observed_at'] = d.Datetime

    d['symbol'] = symbol
    d['observed_at_utc'] = pd.Series([1 for _ in range(len(d.observed_at))],index=d.observed_at).tz_convert('UTC').reset_index()['observed_at']
    d['interval'] = interval_options[interval]
    d.rename(
        columns={
            'Open':"open_price",
            'High': "high_price",
            "Low": "low_price",
            "Close":"close_price",
            "Adj Close": "adj_close",
            "Volume":"volume",
        },
        inplace=True
    )
    return d

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--plugin-name", type=str, required=True, help="Name of plugin - E.G 'offline.offlineScraper'")
    parser.add_argument("--configuration-getter-name", type=str, required=True, help="Name of configuration getter - look into SPFinance.configuration_getter")
    parser.add_argument("--db-host", type=str, required=False, help="Param for offlineScraper - host of postgres database")
    parser.add_argument("--db-host", type=str, required=False, help="Param for offlineScraper - host of postgres database")
    return parser
