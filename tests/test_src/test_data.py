import pytest
from app.src.data import gen_account_copy_to_sql
from app.src.data import gen_transaction_copy_to_sql

def test_gen_account_copy_to_sql(setup_postgres):
    result = gen_account_copy_to_sql().as_string(setup_postgres)
    expect = "COPY account TO STDOUT WITH (FORMAT CSV, DELIMITER ',', HEADER);"
    assert result == expect


def test_gen_transaction_copy_to_sql(setup_postgres):
    result = gen_transaction_copy_to_sql().as_string(setup_postgres)
    expect = "COPY transaction TO STDOUT WITH (FORMAT CSV, DELIMITER ',', HEADER);"
    assert result == expect
