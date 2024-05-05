\c postgres;

CREATE TABLE IF NOT EXISTS account (
    account_id SERIAL,
    name CHARACTER VARYING,
    balance INT
);

CREATE TABLE IF NOT EXISTS transaction (
    transation_id SERIAL,
    account_id CHARACTER VARYING,
    type CHARACTER VARYING,
    amount INT,
    timestamp TIMESTAMP WITHOUT TIME ZONE
);

insert into account(name, balance) values ('Michael', 1000);
insert into account(name, balance) values ('Kay', 0);