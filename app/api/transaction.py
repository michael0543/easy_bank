from fastapi import APIRouter, HTTPException, Depends

from app.models.transaction import DepositCreate
from app.models.transaction import WithdrawCreate
from app.models.transaction import TransferCreate
from app.database.connection import DataBase, get_database

router = APIRouter()


@router.post("/transaction/deposit")
def deposit(
    deposit_data: DepositCreate, db: DataBase = Depends(get_database)
):
    db.deposit(deposit_data)
    return {"message": "Deposit successfully"}


@router.post("/transaction/withdraw")
def withdraw(
    withdraw_data: WithdrawCreate, db: DataBase = Depends(get_database)
):
    try:
        db.withdraw(withdraw_data)
        return {"message": "Withdraw successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/transaction/transfer")
def transfer(
    transfer_data: TransferCreate, db: DataBase = Depends(get_database)
):
    db.transfer(transfer_data)
    return {"message": "Transfer successfully"}
