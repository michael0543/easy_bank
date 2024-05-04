import psycopg2
from typing import Type
from psycopg2.sql import SQL, Literal

def gen_insert_deposit_sql(
        account_id: int, amount: int
) -> Type[psycopg2.sql.Composed]:
    """Generate insert deposit sql into transaction table with given account_id and amount

    Args:
        - account_id: account_id
        - amount: deposit amount
    
    Returns:
        - a insert sql statement
    """
    # sqlstring = f"INSERT INTO transaction(account_id, type, amount, timestamp) "\
    #     f"VALUES ('{account_id}', 'deposit', '{amount}', now());"
    sqlstring = SQL(
        "INSERT INTO transaction(account_id, type, amount, timestamp) "
        "VALUES "
        "({a_id}, 'deposit', {_amount}, now());"
    ).format(
        a_id=Literal(account_id),
        _amount=Literal(amount)
    )
    return sqlstring

def gen_insert_withdraw_sql(
        account_id: int, amount: int
) -> Type[psycopg2.sql.Composed]:
    """Generate insert withdraw sql into transaction table with given account_id and amount
    
    Args:
        - account_id: account_id
        - amount: withdraw amount

    Returns:
        - a insert sql statement 
    """
    sqlstring = f"INSERT INTO transaction(account_id, type, amount, timestamp) "\
        f"VALUES ('{account_id}', 'withdraw', '{amount}', now());"
    sqlstring = SQL(
        "INSERT INTO transaction(account_id, type, amount, timestamp) "
        "VALUES "
        "({a_id}, 'withdraw', {_amount}, now());"
    ).format(
        a_id=Literal(account_id),
        _amount=Literal(amount)
    )
    return sqlstring

def gen_insert_transfer_sql(
        account_id: int, amount: int, trans_type: str
) -> Type[psycopg2.sql.Composed]:
    """Generate insert transfer sql into transaction table with given account_id, amount and trans_type

    Args:
        - account_id: account_id
        - amount: transfer amount
        - trans_type: transaction type. include 'transaction_send' and 'transaction_receive'
    """
    sqlstring = f"INSERT INTO transaction(account_id, type, amount, timestamp) "\
        f"VALUES ('{account_id}', '{trans_type}', '{amount}', now());"
    sqlstring = SQL(
        "INSERT INTO transaction(account_id, type, amount, timestamp) "
        "VALUES "
        "({a_id}, {t_type}, {_amount}, now());"
    ).format(
        a_id=Literal(account_id),
        t_type=Literal(trans_type),
        _amount=Literal(amount)
    )
    return sqlstring