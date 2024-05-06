import psycopg2
from io import BytesIO
from contextlib import contextmanager


from app.models.account import AccountCreate
from app.models.transaction import DepositCreate
from app.models.transaction import WithdrawCreate
from app.models.transaction import TransferCreate
from app.src.account import gen_get_account_id_sql
from app.src.account import gen_get_account_balance_sql
from app.src.account import gen_insert_account_sql
from app.src.account import gen_update_account_balance_sql
from app.src.transaction import gen_insert_deposit_sql
from app.src.transaction import gen_insert_withdraw_sql
from app.src.transaction import gen_insert_transfer_sql
from app.src.data import gen_account_copy_to_sql
from app.src.data import gen_transaction_copy_to_sql


@contextmanager
def get_connection(conn_info: dict):
    conn = psycopg2.connect(**conn_info)
    try:
        yield conn
    except Exception:
        conn.close()


class DataBase:

    def __init__(
            self,
            host: str,
            port: str,
            user: str,
            password: str,
            dbname: str
            ):
        self.conn_info = {
            "host": host,
            "port": port,
            "user": user,
            "password": password,
            "dbname": dbname
        }

    def execute_select_one(self, select_sql: str):
        with get_connection(self.conn_info) as conn:
            with conn.cursor() as cur:
                cur.execute(select_sql)
                result = cur.fetchone()
        return result

    def execute_insert(self, insert_sql: str):
        with get_connection(self.conn_info) as conn:
            with conn.cursor() as cur:
                cur.execute(insert_sql)
            conn.commit()

    def get_account_id(self, account_name: str):
        """Get account_id from account table with given account name"""
        select_sql = gen_get_account_id_sql(name=account_name)
        result, = self.execute_select_one(select_sql)
        return result

    def get_account_balance(self, account_id: int):
        """Get account balance from account table with given account_id"""
        select_sql = gen_get_account_balance_sql(account_id=account_id)
        result, = self.execute_select_one(select_sql)
        return result

    def create_account(self, account_data: AccountCreate):
        """Insert new account data into account table"""
        insert_sql = gen_insert_account_sql(
            name=account_data.name, balance=account_data.balance
        )
        with get_connection(self.conn_info) as conn:
            with conn.cursor() as cur:
                cur.execute(insert_sql)
                result, = cur.fetchone()
            conn.commit()
        return result

    def deposit(self, deposit_data: DepositCreate):
        """
        Deposit Money.
        Insert deposit record into transaction table and update account table.
        """
        account_id = self.get_account_id(deposit_data.name)
        insert_transaction_sql = gen_insert_deposit_sql(
            account_id=account_id,
            amount=deposit_data.amount
        )
        update_account_sql = gen_update_account_balance_sql(
            account_id=account_id,
            amount=deposit_data.amount,
            trans_type="deposit"
        )
        with get_connection(self.conn_info) as conn:
            with conn.cursor() as cur:
                cur.execute(insert_transaction_sql)
                cur.execute(update_account_sql)
            conn.commit()

    def withdraw(self, withdraw_data: WithdrawCreate):
        """
        Withdraw money.
        Insert withdraw record into transaction table and update account table.
        If account balance is not enough, raise ValueError.
        """
        account_id = self.get_account_id(account_name=withdraw_data.name)
        account_balance = self.get_account_balance(account_id=account_id)
        if account_balance < withdraw_data.amount:
            raise ValueError("Account balance is not enough")

        insert_transaction_sql = gen_insert_withdraw_sql(
            account_id=account_id, amount=withdraw_data.amount
        )
        update_account_sql = gen_update_account_balance_sql(
            account_id=account_id,
            amount=withdraw_data.amount,
            trans_type="withdraw"
        )
        with get_connection(self.conn_info) as conn:
            with conn.cursor() as cur:
                cur.execute(insert_transaction_sql)
                cur.execute(update_account_sql)
            conn.commit()

    def transfer(self, transfer_data: TransferCreate):
        """
        Transfer money.
        Insert transfer record into transaction table and update account table.
        """
        sender_id = self.get_account_id(account_name=transfer_data.sender_name)
        receiver_id = self.get_account_id(
            account_name=transfer_data.receiver_name
        )
        insert_transaction_sql = gen_insert_transfer_sql(
            account_id=sender_id,
            amount=transfer_data.amount,
            trans_type="transfer_send"
        ) + gen_insert_transfer_sql(
            account_id=receiver_id,
            amount=transfer_data.amount,
            trans_type="transfer_receive"
        )
        update_account_sql = gen_update_account_balance_sql(
            account_id=sender_id,
            amount=transfer_data.amount,
            trans_type="transfer_send"
        ) + gen_update_account_balance_sql(
            account_id=receiver_id,
            amount=transfer_data.amount,
            trans_type="transfer_receive"
        )
        with get_connection(self.conn_info) as conn:
            with conn.cursor() as cur:
                cur.execute(insert_transaction_sql)
                cur.execute(update_account_sql)
            conn.commit()

        return {"message": "transfer success !"}

    def output_account_csv(self):
        """
        output account table as csv file
        """
        copy_to_sql = gen_account_copy_to_sql()
        in_mem_obj = BytesIO()
        with get_connection(self.conn_info) as conn:
            with conn.cursor() as cur:
                cur.copy_expert(copy_to_sql, in_mem_obj)
                in_mem_obj.seek(0)
        return in_mem_obj

    def output_transaction_csv(self):
        """
        output transaction table as csv file
        """
        copy_to_sql = gen_transaction_copy_to_sql()
        in_mem_obj = BytesIO()
        with get_connection(self.conn_info) as conn:
            with conn.cursor() as cur:
                cur.copy_expert(copy_to_sql, in_mem_obj)
                in_mem_obj.seek(0)
        return in_mem_obj


def get_database():
    host = "db"
    port = "5432"
    user = "postgres"
    password = "postgres"
    dbname = "postgres"

    db = DataBase(
        host=host, port=port, user=user, password=password, dbname=dbname
    )
    try:
        yield db
    finally:
        pass
