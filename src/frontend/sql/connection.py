from frontend.sql.collections.stock import Stock
  

if __name__ == '__main__': 
    stock = Stock(db_name="finance", config_path="src/frontend/sql/connection.json")
    
    doc = {
        "symbol": "'CAST'",
        "open_price": '132',
        "close_price": '100'
    }
    print(stock.get_documents())
    # print(stock.add_document(document=doc))
