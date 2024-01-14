from SPFinance.database_connection.collections.stock import Stock

  

def stock_start():
    stock = Stock(db_name="finance", config_path="src\SPFinance\database_connection\connection.json")
    
    doc = {
        "symbol": "'CAST'",
        "open_price": '132',
        "close_price": '100'
    }
    return stock.get_documents()
    # print(stock.add_document(document=doc))