import pandas as pd
import yfinance as yf
from sqlalchemy import create_engine


class offlineScraper:
    def __init__(
        self,
        db_host,
        db_name,
        db_user_name,
        db_user_password,
    ):
        self.engine = create_engine(f"postgresql+psycopg2://{db_user_name}:{db_user_password}@{db_host}/{db_name}")



    def load_stock_into_database()
