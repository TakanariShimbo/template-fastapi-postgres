## About

Template FastAPI x Postgres

ref: https://fastapi.tiangolo.com/tutorial/sql-databases/#technical-details-about-orm-mode

## Usage

### Build API Server Image

```sh
cd api_server
docker build -t fastapi_server .
```

### Docker Compose Up

```sh
# ensure .env is set before running the following command.
docker compose up -d
```
