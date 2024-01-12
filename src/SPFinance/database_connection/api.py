import json
import psycopg

class Api:
    
    def __init__(self, db_name, collection, config_path='') -> None:
        self.host = None
        self.port = None
        self.database = db_name
        self.collection = collection
        self.user = None
        self.password = None
        
        self.connect = False
        self.reconnect = {
            "allow": False,
            "wait_time": 10,
            "nr_of_retry": 6
        }
        
        self.db_name = db_name
        self.collection = collection
        self.config_path = config_path
        
        self._connect()
        
    def _connect(self):
        with open(self.config_path, 'r') as config:
            data = json.loads(config.read())
            self.host = data["host"]
            self.port = data["port"]
            self.user = data["user"]
            self.password = data["password"]
            if data["connect"]: 
                self.connect = data["connect"]
        
        self.client = psycopg.connect("dbname={dbname} port={port} user={user} password={password} host={host}"
                                      .format(dbname = self.database, port = self.port, user = self.user, password = self.password, host = self.host))
        self.cursor = self.client.cursor()
        
        
    
    def get_documents(self):
        """
        Get all documents from collection
        """
        try:
            data = self.cursor.execute("""
                                SELECT * FROM {collection}
                                """.format(collection=self.collection)).fetchall()    
        except BaseException as be:
            print("ERROR: ", be)
        
        return data
    
    
    def get_document(self, filter=None):
        """
        Get document from collection
        """
        try:
            self.client.execute(
                """
                SELECT * FROM {collection} WHERE {filter}
                """.format(
                    collection = self.collection,
                    filter = filter
                )
            ).fetchall()
        except BaseException as be:
            print("ERROR: ", be)
            self.client.rollback()
    
    
    def add_document(self, document):
        """
        Add document to the collection
        """
        try:
            self.client.execute(
                "INSERT INTO {collection} ({columns}) VALUES ({values});"
                    .format(collection=self.collection, 
                            columns=', '.join(document.keys()), 
                            values=", ".join(document.values()))
            )
        except BaseException as be:
            print("ERROR: ", be)
            self.client.rollback()
        else:
            print("commited")
            self.client.commit()
    

    def update_document(self, document):
        """
        Update document in collection
        """

