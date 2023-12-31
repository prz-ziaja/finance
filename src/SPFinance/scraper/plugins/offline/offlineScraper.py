import datetime as dt
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
from SPFinance.scraper import get_stock
from SPFinance.scraper.abstractScraper import abstractOfflineScraper


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
        super(abstractOfflineScraper, self).__init__("offline_scraper", objects_to_scrap, db_host, configuration_getter_name,**configuration_getter_args)
        self.start_datetime = dt.datetime(start_datetime)
        self.end_datetime = dt.datetime(end_datetime)
        self.interval = interval
        self.multiproc_manager = multiprocessing.Manager()
        self.lock = self.multiproc_manager.Lock()

    def load_stock_into_database(self, symbol):
        stock_data = get_stock(symbol, self.start_datetime, self.end_datetime, self.interval)
        with self.lock:
            stock_data.to_sql('stock', self.engine, if_exists='append', index=False)

    def run(self):
        pool = ProcessPoolExecutor()
        jobs = [pool.submit(self.load_stock_into_database, symbol) for symbol in self.objects_to_scrap]
        [job.result() for job in jobs]
