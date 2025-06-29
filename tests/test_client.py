"""Tests for clickhouse_connector/client.py"""

import pytest
from unittest.mock import patch, MagicMock
from clickhouse_connector.client import get_clickhouse_client
from clickhouse_connector.config import ClickHouseCredentials

@patch("clickhouse_connector.client.get_credentials")
@patch("clickhouse_connector.client.get_client")
def test_get_clickhouse_client_returns_client(mock_get_client, mock_get_credentials):
    mock_get_credentials.return_value = ClickHouseCredentials(
        host="localhost",
        port=8123,
        username="default",
        password="pass4admin",
        database="default"
    )

    mock_client = MagicMock()
    mock_get_client.return_value = mock_client

    client = get_clickhouse_client(env="lab")

    assert client == mock_client
    mock_get_credentials.assert_called_once_with("lab")
    mock_get_client.assert_called_once_with(
        host="localhost",
        port=8123,
        username="default",
        password="pass4admin",
        database="default"
    )
