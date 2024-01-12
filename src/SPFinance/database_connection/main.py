from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from SPFinance.database_connection.collections.stock import Stock


stock = Stock(db_name="finance", config_path="/app/SPFinance/database_connection/connection.json")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
@app.get("/index/")
def home():
    return {"success": "Great Success"}


@app.get("/items")
def items():
    return stock.get_documents()