from app.collections.collection_generic import CollectionGeneric
from datetime import datetime

class Stock(CollectionGeneric):
    
    def __init__(self, db_name, config_path=''):
        super().__init__(db_name, collection='stock', config_path=config_path)
        
    def get_documents(self):
        documents = self.api.get_documents()
        
        data = []
        
        for document in documents:
            data.append(list(document))
            
        for id in range(len(data)):
            data[id][2] = data[id][2].timestamp()*1000
        return data
    
    def add_document(self, document):
        self.api.add_document(document)
        
    def update_document(self, document):
        self.api.update_document(document)