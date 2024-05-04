from fastapi import APIRouter, HTTPException, Depends


from app.models.account import Account, AccountCreate, AccountUpdate
from app.database.connection import DataBase, get_database

router = APIRouter()

@router.post("/accounts")
def create_account(account_data: AccountCreate, db: DataBase = Depends(get_database)):
    account_id = db.create_account(account_data)
    msg = {
        "message": "Account created successfully",
        "account_id": account_id
    }
    return msg

# @app.post("/accounts/", response_model=int)
# def create_account(account_data: AccountCreate):
#     account_id = account_service.create_account(account_data.name, account_data.balance)
#     return account_id

# @app.post("/accounts/{account_id}/deposit/", response_model=int)
# def deposit(account_id: int, amount: int):
#     new_balance = account_service.deposit(account_id, amount)
#     return new_balance

# @app.post("/accounts/{account_id}/withdraw/", response_model=int)
# def withdraw(account_id: int, amount: int):
#     new_balance = account_service.withdraw(account_id, amount)
#     return new_balance