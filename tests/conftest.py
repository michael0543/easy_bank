import os
import pytest
import psycopg2
from testcontainers.postgres import PostgresContainer


@pytest.fixture(scope="module", autouse=True)
def setup_postgres():
    postgres_container = PostgresContainer(
        image="postgres:14", user="postgres", password="postgres", driver="psycopg2",
    )
    postgres_container.with_volume_mapping(
        os.path.abspath("tests/init.sql"), "/docker-entrypoint-initdb.d/init.sql"
    )
    
    with postgres_container as postgres:
        conn_info = {
            "host": postgres.get_container_host_ip(),
            "port": postgres.get_exposed_port(postgres.port_to_expose),
            "user": "postgres",
            "password": "postgres",
            "dbname": "postgres"
        }
        conn = psycopg2.connect(**conn_info)
        yield conn