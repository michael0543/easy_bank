from pydantic import BaseModel
from datetime import datetime


class TransactionBase(BaseModel):
    amount: int
    timestamp: datetime


class TransactionCreate(BaseModel):
    account_id: int
    type: str
    amount: int


class Transaction(BaseModel):
    transaction_id: int
    account_id: int
    type: str
    amount: str
    timestamp: datetime


class DepositCreate(BaseModel):
    name: str
    amount: int


class WithdrawCreate(BaseModel):
    name: str
    amount: int


class TransferCreate(BaseModel):
    sender_name: str
    receiver_name: str
    amount: int
