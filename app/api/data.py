from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from app.database.connection import DataBase, get_database

router = APIRouter()


@router.get("/data/account")
def output_account_data(db: DataBase = Depends(get_database)):
    data = db.output_account_csv()
    response = StreamingResponse(
        data,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=account.csv"}
    )
    return response


@router.get("/data/transaction")
def output_transaction_data(db: DataBase = Depends(get_database)):
    data = db.output_transaction_csv()
    response = StreamingResponse(
        data,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=transaction.csv"}
    )
    return response
