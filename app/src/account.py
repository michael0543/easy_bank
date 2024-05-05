import psycopg2
from typing import Type
from psycopg2.sql import SQL, Literal


def gen_get_account_id_sql(name: str) -> Type[psycopg2.sql.Composed]:
    """Generate select account_id sql from account table with given name.

    Args:
        - name: account name

    Returns:
        - a select sql statement
    """
    sqlstring = SQL(
        "SELECT account_id "
        "FROM account "
        "WHERE name={a_name};"
    ).format(
        a_name=Literal(name)
    )
    return sqlstring


def gen_get_account_balance_sql(
        account_id: int
) -> Type[psycopg2.sql.Composed]:
    """Generate select balance sql from account table with given account_id

    Args:
        - account_id: account_id

    Returns:
        - a select sql statement
    """
    sqlstring = SQL(
        "SELECT balance "
        "FROM account "
        "WHERE account_id={a_id};"
    ).format(
        a_id=Literal(account_id)
    )
    return sqlstring


def gen_insert_account_sql(
        name: str, balance: int = 0
) -> Type[psycopg2.sql.Composed]:
    """Generate insert sql into account table with given name and balance

    Args:
        - name: account name
        - balance: account balance, default is 0

    Returns:
        - a insert sql statement
    """
    sqlstring = SQL(
        "INSERT INTO account(name, balance) "
        "VALUES "
        "({a_name}, {a_balance}) "
        "RETURNING account_id;"
    ).format(
        a_name=Literal(name),
        a_balance=Literal(balance)
    )

    return sqlstring


def gen_update_account_balance_sql(
        account_id: int, amount: int, trans_type: str
) -> Type[psycopg2.sql.Composed]:
    """Generate update balance sql in account table with given \
        account_id, update amount and update type

    Args:
        - account_id: account_id
        - amount: update amount
        - type: transaction type. include 'deposit', 'withdraw', \
            'transfer_send', 'transfer_receive'

    Returns:
        - a update sql statement
    """
    if trans_type == "deposit" or trans_type == "transfer_receive":
        set_balance = SQL(
            "balance=balance+{_amount}"
        ).format(
            _amount=Literal(amount)
        )
    elif trans_type == "withdraw" or trans_type == "transfer_send":
        set_balance = SQL(
            "balance=balance-{_amount}"
        ).format(
            _amount=Literal(amount)
        )
    sqlstring = SQL(
        "UPDATE account "
        "SET {_set_balance} "
        "WHERE account_id={a_id};"
    ).format(
        _set_balance=set_balance,
        a_id=Literal(account_id)
    )

    return sqlstring
