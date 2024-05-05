from fastapi import APIRouter, Depends


from app.models.account import AccountCreate
from app.database.connection import DataBase, get_database

router = APIRouter()


@router.post("/accounts")
def create_account(
    account_data: AccountCreate, db: DataBase = Depends(get_database)
):
    account_id = db.create_account(account_data)
    msg = {
        "message": "Account created successfully",
        "account_id": account_id
    }
    return msg
