import pandas as pd
import yfinance as yf
from sqlalchemy import create_engine
from SPFinance.scraper import get_stock


class abstractOfflineScraper:
    def __init__(
        self,
        db_host:str,
        db_name:str,
        db_user_name:str,
        db_user_password:str,
        objects_to_scrap:list,
    ):
        self.engine = create_engine(f"postgresql+psycopg2://{db_user_name}:{db_user_password}@{db_host}/{db_name}")
        self.objects = objects_to_scrap

    def run(self):
        raise NotImplementedError("Method run not implemented")

class abstractOnlineScraper:
    def __init__(
        self,

        objects_to_scrap:list,
    ):
        self.engine = create_engine(f"postgresql+psycopg2://{db_user_name}:{db_user_password}@{db_host}/{db_name}")
        self.objects = objects_to_scrap

    def run(self):
        raise NotImplementedError("Method run not implemented")