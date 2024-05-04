import psycopg2
from typing import Type
from psycopg2.sql import SQL

def gen_account_copy_to_sql() -> Type[psycopg2.sql.Composed]:
    """Generate copy to sql of account table

    Returns:
        - a copy to sql statement
    """
    sqlstring = SQL(
        "COPY account TO STDOUT WITH (FORMAT CSV, DELIMITER ',', HEADER);"
    )
    return sqlstring

def gen_transaction_copy_to_sql() -> Type[psycopg2.sql.Composed]:
    """Generate copy to sql of transaction table

    Returns:
        - a copy to sql statement
    """
    sqlstring = SQL(
        "COPY transaction TO STDOUT WITH (FORMAT CSV, DELIMITER ',', HEADER);"
    )
    return sqlstring