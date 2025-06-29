# ClickHouse Connector

A small Python module for initializing a ClickHouse client based on environment-specific credentials.

## Features

- Supports `lab`, `development`, and `production` environments
- Loads credentials from `.env` or environment variables
- Validates required fields before client creation

---

## Project Structure

```arduino
clickhouse-connector/
├── clickhouse_connector/
│   ├── __init__.py
│   ├── client.py
│   └── config.py
├── tests/
│   ├── __init__.py
│   ├── test_client.py
│   └── test_config.py
├── .env
├── .gitignore
├── .python-version
├── LICENSE
├── .pyproject.toml
├── README.md
└── uv.lock
```

## Environment Variables
Create a .env file in your project root with the following structure:
```env
LAB_CLICKHOUSE_HOST=lab.example.com
LAB_CLICKHOUSE_PORT=8123
LAB_CLICKHOUSE_USER=lab_user
LAB_CLICKHOUSE_PASS=lab_pass
LAB_CLICKHOUSE_DB=default

DEV_CLICKHOUSE_HOST=localhost
DEV_CLICKHOUSE_PORT=8123
DEV_CLICKHOUSE_USER=default
DEV_CLICKHOUSE_PASS=dev_pass
DEV_CLICKHOUSE_DB=default

PROD_CLICKHOUSE_HOST=prod.example.com
PROD_CLICKHOUSE_PORT=8123
PROD_CLICKHOUSE_USER=admin
PROD_CLICKHOUSE_PASS=secure_pass
PROD_CLICKHOUSE_DB=default
```

## License
License: MIT — see [LICENSE](LICENSE) for full text.
