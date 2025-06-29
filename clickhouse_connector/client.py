"""
Get a ClickHouse client to interact with a ClickHouse database.
"""
from clickhouse_connect import get_client
from .config import get_credentials, ClickHouseCredentials


def get_clickhouse_client(env='lab'):
    """
    Initializes and returns a ClickHouse client using credentials
    for the specifcied deployment environment.

    Args:
        env (str): The target environment (e.g., 'development', 'lab', or 'production').

    Returns:
        clickhouse_connect.driver.client.Client: A ClickHouse client instance.

    Raises:
        ValueError: If the specified environment is invalid or required credentials are missing (from get_credentials()).
    """
    creds: ClickHouseCredentials = get_credentials(env)
    return get_client(
        host=creds.host,
        port=creds.port,
        username=creds.username,
        password=creds.password,
        database=creds.database
    )
