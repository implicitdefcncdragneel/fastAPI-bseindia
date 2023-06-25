from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from models import Deals

app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url="postgresql+psycopg2://admin:admin@bsedb:5432/bsedeals")

@app.get("/")
def list_deals():
    deals = db.session.query(Deals).all()
    return {"deals": deals}
