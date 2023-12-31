import pandas as pd
import yfinance as yf
from sqlalchemy import create_engine
from copy import copy
import importlib


class abstractScraper:
    def __init__(self, name):
        self.component_name = name

    def get_name(self):
        return copy(self.component_name)
 
    def get_configuration(self, configuration_getter_name:str, **configuration_getter_args):
        config_module = importlib.import_module(f"SPFinance.configuration_getter.{configuration_getter_name}")
        self.config = config_module.get_configuration(self.get_name(), **configuration_getter_args)


class abstractOfflineScraper(abstractScraper):
    def __init__(
        self,
        name:str,
        objects_to_scrap:list,
        db_host:str,
        configuration_getter_name:str,
        **configuration_getter_args
    ):
        super(abstractScraper, self).__init__(name)
        self.get_configuration(configuration_getter_name, **configuration_getter_args)
        self.engine = create_engine(f"postgresql+psycopg2://{self.config['db_user_name']}:{self.config['db_user_password']}@{db_host}/{self.config['db_name']}")
        self.objects = objects_to_scrap

    def run(self):
        raise NotImplementedError("Method run not implemented")


class abstractOnlineScraper(abstractScraper):
    def __init__(
        self,
        name:str,
        objects_to_scrap:list,
        configuration_getter_name:str,
        **configuration_getter_args
    ):
        super(abstractScraper, self).__init__(name)
        self.objects = objects_to_scrap
        self.get_configuration(configuration_getter_name, **configuration_getter_args)

    def run(self):
        raise NotImplementedError("Method run not implemented")
