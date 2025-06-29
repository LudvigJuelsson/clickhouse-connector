"""Tests for clickhouse_connector/config.py"""

import pytest
from clickhouse_connector.config import get_credentials, ClickHouseCredentials

@pytest.fixture
def set_dev_env(monkeypatch):
    monkeypatch.setenv("DEV_CLICKHOUSE_HOST", "localhost")
    monkeypatch.setenv("DEV_CLICKHOUSE_PORT", "9000")
    monkeypatch.setenv("DEV_CLICKHOUSE_USER", "tester")
    monkeypatch.setenv("DEV_CLICKHOUSE_PASS", "secret")
    monkeypatch.setenv("DEV_CLICKHOUSE_DB", "test_db")

def test_get_credentials_valid_env(set_dev_env):
    creds = get_credentials("development")
    assert isinstance(creds, ClickHouseCredentials)
    assert creds.host == "localhost"
    assert creds.port == 9000
    assert creds.username == "tester"
    assert creds.password == "secret"
    assert creds.database == "test_db"

def test_invalid_environment_raises():
    with pytest.raises(ValueError):
        get_credentials("staging")  # not supported
