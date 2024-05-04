from contextlib import closing
from fastapi import FastAPI
# from pydantic import BaseModel

# from src.account import insert_account
# from models.account import AccountCreate
# from database.connection import get_conn

from app.api import account
from app.api import transaction
from app.api import data

app = FastAPI()

# @app.post("/account/create/")
# def create_account(account: AccountCreate):
#     with closing(get_conn()) as conn:
#         insert_account(conn, account.name, account.balance)
#     return {"create account": "success"}

app.include_router(account.router, prefix="/api")
app.include_router(transaction.router, prefix="/api")
app.include_router(data.router, prefix="/api")