CREATE TABLE IF NOT EXISTS transaction (
    transation_id SERIAL,
    accout_id CHARACTER VARYING,
    type CHARACTER VARYING,
    amount INT,
    timestamp TIMESTAMP WITHOUT TIME ZONE
);