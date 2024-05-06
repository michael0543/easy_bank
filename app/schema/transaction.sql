CREATE TABLE IF NOT EXISTS transaction (
    transation_id SERIAL,
    account_id CHARACTER VARYING,
    type CHARACTER VARYING,
    amount INT,
    timestamp TIMESTAMP WITHOUT TIME ZONE
);