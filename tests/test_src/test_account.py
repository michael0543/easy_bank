import pytest

from app.src.account import gen_get_account_id_sql
from app.src.account import gen_get_account_balance_sql
from app.src.account import gen_insert_account_sql
from app.src.account import gen_update_account_balance_sql

def test_gen_get_account_id_sql(setup_postgres):
    _name = "Kobe Bryant"
    result = gen_get_account_id_sql(name=_name).as_string(setup_postgres)
    expect = "SELECT account_id FROM account WHERE name='Kobe Bryant';"
    assert result == expect


def test_gen_get_account_balance_sql(setup_postgres):
    _id = 1
    result = gen_get_account_balance_sql(account_id=_id).as_string(setup_postgres)
    expect = "SELECT balance FROM account WHERE account_id=1;"
    assert result == expect


def test_gen_insert_account_sql(setup_postgres):
    _name = "Magic Johnson"
    _balance = 3200
    result = gen_insert_account_sql(name=_name, balance=_balance).as_string(setup_postgres)
    expect = "INSERT INTO account(name, balance) VALUES ('Magic Johnson', 3200) RETURNING account_id;"
    assert result == expect


@pytest.mark.parametrize(
        "_account_id, _amount, _type, expect",
        [
            (
                1, 1000, "deposit",
                "UPDATE account SET balance=balance+1000 WHERE account_id=1;"
            ),
            (
                1, 1000, "withdraw",
                "UPDATE account SET balance=balance-1000 WHERE account_id=1;"
            ),
            (
                2, 2000, "transfer_send",
                "UPDATE account SET balance=balance-2000 WHERE account_id=2;"
            ),
            (   2, 2000, "transfer_receive",
                "UPDATE account SET balance=balance+2000 WHERE account_id=2;"
            )
        ]
)
def test_gen_update_account_balance_sql(
    _account_id, _amount, _type, expect, setup_postgres
):
    result = gen_update_account_balance_sql(account_id=_account_id, amount=_amount, type=_type).as_string(setup_postgres)
    assert result == expect