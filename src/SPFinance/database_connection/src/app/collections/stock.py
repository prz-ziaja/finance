from app.collections.collection_generic import CollectionGeneric
from datetime import datetime

class Stock(CollectionGeneric):
    
    def __init__(self, db_name, config_path=''):
        super().__init__(db_name, collection='stock', config_path=config_path)
        
    def get_documents(self):
        documents = self.api.get_documents()
        data = self.detuplify(documents)        

        for id in range(len(data)):
            data[id][2] = data[id][2].timestamp()*1000
        return data
    
    
    def get_companies(self):
        documents = self.api.get_columns(column="symbol")
        data = set([element[0] for element in self.detuplify(documents)])
        return data
    
    
    def add_document(self, document):
        self.api.add_document(document)
        
        
    def update_document(self, document):
        self.api.update_document(document)
    
    
    def get_company(self, company_name):
        documents = self.api.get_document(filter="symbol='{}'".format(company_name))
        data = self.detuplify(documents)
        
        for id in range(len(data)):
            data[id][2] = data[id][2].timestamp()*1000
        
        return data
        
        
    def detuplify(self, documents):
        return [list(document) for document in documents]
    