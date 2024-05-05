import pytest


from app.src.transaction import gen_insert_deposit_sql
from app.src.transaction import gen_insert_withdraw_sql
from app.src.transaction import gen_insert_transfer_sql


def test_gen_insert_deposit_sql(setup_postgres):
    _account_id = 1
    _amount = 1000
    result = gen_insert_deposit_sql(account_id=_account_id, amount=_amount).as_string(setup_postgres)
    expect = "INSERT INTO transaction(account_id, type, amount, timestamp) "\
        "VALUES (1, 'deposit', 1000, now());"
    assert result == expect


def test_gen_insert_withdraw_sql(setup_postgres):
    _account_id = 2
    _amount = 2000
    result = gen_insert_withdraw_sql(account_id=_account_id, amount=_amount).as_string(setup_postgres)
    expect = "INSERT INTO transaction(account_id, type, amount, timestamp) "\
        "VALUES (2, 'withdraw', 2000, now());"
    assert result == expect


@pytest.mark.parametrize(
        "_account_id, _amount, _trans_type, expect",
        [
            (
                1, 1000, "transfer_send",
                "INSERT INTO transaction(account_id, type, amount, timestamp) "\
                "VALUES (1, 'transfer_send', 1000, now());"
             ),
            (
                2, 2000, "transfer_receive",
                "INSERT INTO transaction(account_id, type, amount, timestamp) "\
                "VALUES (2, 'transfer_receive', 2000, now());"
            )
        ]
)
def test_gen_insert_transfer_sql(_account_id, _amount, _trans_type, expect, setup_postgres):
    result = gen_insert_transfer_sql(account_id=_account_id, amount=_amount, trans_type=_trans_type).as_string(setup_postgres)
    assert result == expect
