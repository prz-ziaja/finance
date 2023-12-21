import pandas as pd
import yfinance as yf
from sqlalchemy import create_engine


class offlineScraper:
    def __init__(
        self,
        db_address,
        db_user_name,
    ):
        self.engine = create_engine(db_address)
