from typing import Optional
from pydantic import BaseModel


class Account(BaseModel):
    account_id: int
    name: str
    balance: int


class AccountCreate(BaseModel):
    name: str
    balance: Optional[int] = 0


class AccountUpdate(BaseModel):
    name: str
    balance: int


class AccountName(BaseModel):
    name: str
