import pandas as pd
import yfinance as yf
from sqlalchemy import create_engine
from SPFinance.scraper import get_stock
from SPFinance.scraper.abstractScraper import abstractOfflineScraper


class offlineScraper(abstractOfflineScraper):
    def __init__(
        self,
        db_host,
        db_name,
        db_user_name,
        db_user_password,
    ):
        super(abstractOfflineScraper, self).__init__(db_host, db_name, db_user_name, db_user_password)
        self.engine = create_engine(f"postgresql+psycopg2://{db_user_name}:{db_user_password}@{db_host}/{db_name}")

    def load_stock_into_database(self, symbol, start_datetime, end_datetime, interval):
        stock_data = get_stock(symbol, start_datetime, end_datetime, interval)
        stock_data.to_sql('stock', self.engine, if_exists='append', index=False)
