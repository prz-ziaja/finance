from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.collections.stock import Stock


stock = Stock(db_name="finance", config_path="/app/app/connection.json")

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


@app.get("/stock/items")
def items():
    return stock.get_documents()


@app.get("/offline-scraper")
def offline_scraper():
    try:
        # TODO 
        #kod do wystartowania offline scrapera
        return {"success":"Scraper Started"}
    except BaseException as err:
        return {"error": str(err)}
    
    
@app.get("/company/{company_name}")
def get_company(company_name: str):
    return stock.get_company(company_name)

@app.get("/companies")
def get_companies():
    return stock.get_companies()
