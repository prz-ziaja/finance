from app.api import Api


class CollectionGeneric:
    def __init__(self, db_name, collection, config_path=''):
        self.api = Api(db_name, collection, config_path)