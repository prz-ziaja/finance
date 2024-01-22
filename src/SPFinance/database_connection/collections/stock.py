from SPFinance.database_connection.collections.collection_generic import CollectionGeneric

class Stock(CollectionGeneric):
    
    def __init__(self, db_name, config_path=''):
        super().__init__(db_name, collection='stock', config_path=config_path)
        
    def get_documents(self):
        return {"stock": self.api.get_documents()}
    
    def add_document(self, document):
        self.api.add_document(document)
        
    def update_document(self, document):
        self.api.update_document(document)