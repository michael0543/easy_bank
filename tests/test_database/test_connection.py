from app.database.connection import DataBase
from app.models.account import AccountCreate
from app.models.transaction import DepositCreate
from app.models.transaction import WithdrawCreate
from app.models.transaction import TransferCreate


def test_execute_select_one(setup_postgres):
    db = DataBase(
        host=setup_postgres.get_dsn_parameters()["host"],
        port=setup_postgres.get_dsn_parameters()["port"],
        user="postgres",
        password="postgres",
        dbname="postgres"
    )
    select_sql = "SELECT name FROM account WHERE name='Michael';"
    result = db.execute_select_one(select_sql)
    expect = ("Michael",)
    assert result == expect


def test_execute_insert_sql(setup_postgres):
    db = DataBase(
        host=setup_postgres.get_dsn_parameters()["host"],
        port=setup_postgres.get_dsn_parameters()["port"],
        user="postgres",
        password="postgres",
        dbname="postgres"
    )
    insert_sql = "INSERT INTO account(name, balance) "\
        "VALUES ('Lebron James', 0);"
    db.execute_insert(insert_sql)
    select_sql = "SELECT name FROM account WHERE name='Lebron James';"
    result = db.execute_select_one(select_sql)
    expect = ("Lebron James",)
    assert result == expect


def test_get_account_id(setup_postgres):
    db = DataBase(
        host=setup_postgres.get_dsn_parameters()["host"],
        port=setup_postgres.get_dsn_parameters()["port"],
        user="postgres",
        password="postgres",
        dbname="postgres"
    )
    account_name = "Michael"
    result = db.get_account_id(account_name)
    expect = 1
    assert result == expect


def test_get_account_balance(setup_postgres):
    db = DataBase(
        host=setup_postgres.get_dsn_parameters()["host"],
        port=setup_postgres.get_dsn_parameters()["port"],
        user="postgres",
        password="postgres",
        dbname="postgres"
    )
    account_name = "Michael"
    account_id = db.get_account_id(account_name)
    result = db.get_account_balance(account_id)
    expect = 1000
    assert result == expect


def test_create_account(setup_postgres):
    db = DataBase(
        host=setup_postgres.get_dsn_parameters()["host"],
        port=setup_postgres.get_dsn_parameters()["port"],
        user="postgres",
        password="postgres",
        dbname="postgres"
    )
    account_data = AccountCreate(name="Anthony Davis", balance=500)
    result = db.create_account(account_data)
    expect = 4
    assert result == expect


def test_deposit(setup_postgres):
    db = DataBase(
        host=setup_postgres.get_dsn_parameters()["host"],
        port=setup_postgres.get_dsn_parameters()["port"],
        user="postgres",
        password="postgres",
        dbname="postgres"
    )
    deposit_data = DepositCreate(name="Kay", amount=200)
    db.deposit(deposit_data=deposit_data)
    account_balance = db.get_account_balance(account_id=2)
    expect = 200
    assert account_balance == expect


def test_withdraw(setup_postgres):
    db = DataBase(
        host=setup_postgres.get_dsn_parameters()["host"],
        port=setup_postgres.get_dsn_parameters()["port"],
        user="postgres",
        password="postgres",
        dbname="postgres"
    )
    withdraw_data = WithdrawCreate(name="Kay", amount=200)
    db.withdraw(withdraw_data=withdraw_data)
    account_balance = db.get_account_balance(account_id=2)
    expect = 0
    assert account_balance == expect


def test_transfer(setup_postgres):
    db = DataBase(
        host=setup_postgres.get_dsn_parameters()["host"],
        port=setup_postgres.get_dsn_parameters()["port"],
        user="postgres",
        password="postgres",
        dbname="postgres"
    )
    transfer_data = TransferCreate(
        sender_name="Michael", receiver_name="Kay", amount=500
    )
    db.transfer(transfer_data)
    sender_balance = db.get_account_balance(account_id=1)
    receiver_balance = db.get_account_balance(account_id=2)
    sender_balance_expect = 500
    receiver_balance_expect = 500
    assert sender_balance == sender_balance_expect
    assert receiver_balance == receiver_balance_expect
