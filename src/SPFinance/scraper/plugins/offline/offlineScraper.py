import datetime as dt
import multiprocessing
from concurrent.futures import ProcessPoolExecutor, wait
from SPFinance.scraper import get_stock
from SPFinance.scraper.abstractScraper import abstractOfflineScraper, abstractScraper
from SPFinance.scraper.common import DATETIME_FORMAT


class offlineScraper(abstractOfflineScraper):
    def __init__(
        self,
        objects_to_scrap:list,
        db_host:str,
        configuration_getter_name:str,
        start_datetime: str,
        end_datetime: str,
        interval: str,
        **configuration_getter_args
    ):
        abstractOfflineScraper.__init__(self,name="offline_scraper", objects_to_scrap=objects_to_scrap, db_host=db_host, configuration_getter_name=configuration_getter_name,**configuration_getter_args)
        self.start_datetime = dt.datetime.strptime(start_datetime, DATETIME_FORMAT)
        self.end_datetime = dt.datetime.strptime(end_datetime, DATETIME_FORMAT)
        self.interval = interval
        self.objects_to_scrap = objects_to_scrap
        self.multiproc_manager = multiprocessing.Manager()
        self.lock = self.multiproc_manager.Lock()

    def load_stock_into_database(self, symbol):
        stock_data = get_stock(symbol, self.start_datetime, self.end_datetime)
        with self.lock:
            print(f"loading into db {symbol}")
            stock_data.to_sql('stock', self.engine, if_exists='append', index=False)

    def run(self):
        for object_to_scrap in self.objects_to_scrap:
            self.load_stock_into_database(object_to_scrap)
        return
        pool = ProcessPoolExecutor(2)
        jobs = [pool.submit(self.load_stock_into_database, symbol) for symbol in self.objects_to_scrap]
        wait(jobs)
