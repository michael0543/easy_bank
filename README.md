# Easy Bank

This is a simple bank application that allows a user to create an account, deposit money, withdraw money, and transfer money.

## Technologies used:
- FastAPI (Pydantic, psycopg2)
- PostgreSQL
- Docker
- Docker-compose

## Testing:

use follow tools for unit test
- Pytest
- Testcontainer

## Available endpoints:

- `POST /api/accounts/` - create new account
- `POST /api/transaction/deposit/` - to deposit money
- `POST /api/transaction/withdraw/` - to withdraw money
- `POST /api/transaction/transfer` - to transfer money
- `GET /api/data/account/` - download account table as csv file
- `GET /api/data/transaction/` - download transaction table as csv file

About relevent data model, you can go to app/models.

## How to run the application (docker-compose)

Prerequisite: to run the application, you need to have docker and docker-compose installed on your machine.

you can download it from [here](https://www.docker.com/products/docker-desktop).

After you have docker and docker-compose installed, you can clone the repository with:

```
git clone https://github.com/michael/easy_bank.git
```

You need to enter this folder, and then you can run the application with:

```
docker compose up -d 
```

And that's all! The application is running on http://localhost:8000.


To stop the application, you can run:

```
docker compose down
```

## How to see the application in action

Open the browser and go to http://localhost:8000/docs.
You will see the FastAPI Swagger UI where you can test the application.
