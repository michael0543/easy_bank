from fastapi import FastAPI

from app.api import account
from app.api import transaction
from app.api import data

app = FastAPI()

app.include_router(account.router, prefix="/api")
app.include_router(transaction.router, prefix="/api")
app.include_router(data.router, prefix="/api")
