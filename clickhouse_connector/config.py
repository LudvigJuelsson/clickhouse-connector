"""
Config for getting ClickHouse credentials depending on deployment environment.
Add/Remove credential definitions depending on need. 
"""
import os
from dotenv import load_dotenv
from dataclasses import dataclass
import logging
from logging import Logger

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger: Logger = logging.getLogger(__name__)


@dataclass
class ClickHouseCredentials:
    """
    A data class representing credentials required to connect to a ClickHouse database.

    Attributes:
        host (str): The hostname or IP address of the ClickHouse server.
        port (int): The port number the server is listening on.
        username (str): Username used for authentication.
        password (str): Password used for authentication.
        database (str): The database name to connect to.
    """

    host: str
    port: int
    username: str
    password: str
    database: str

    def validate(self):
        """
        Validates that all credentials are present.

        Raises:
            ValueError: If any field is missing.
        """
        missing: list[str] = []
        if not self.host:
            missing.append('host')
        if not self.port:
            missing.append('port')
        if not self.username:
            missing.append('username')
        if not self.password:
            missing.append('password')
        if not self.database:
            missing.append('database')

        if missing:
            raise ValueError(f"Missing required credentials: {', '.join(missing)}")

        logger.debug(f"ClickHouse credentials validated for host: {self.host}")


def get_credentials(env: str = 'development') -> ClickHouseCredentials:
    """
    Loads and returns ClickHouse credentials for the specified deployment environment.

    The function reads credentials from environment variables, which can be
    loaded from a .env file using `python-dotenv`.

    Args:
        env (str): The target environment. Must be one of:
                   'lab', 'development', or 'production'.

    Returns:
        ClickHouseCredentials: An instance populated with environment-specific credentials.

    Raises:
        ValueError: If the environment name is invalid or required credentials are missing.
    """
    prefix_map: dict[str, str] = {
        'lab': 'LAB',
        'development': 'DEV',
        'production': 'PROD'
    }

    prefix: str | None = prefix_map.get(env.lower())
    if not prefix:
        raise ValueError(f"Invalid environment: {env}")

    credentials: ClickHouseCredentials = ClickHouseCredentials(
        host=os.getenv(f'{prefix}_CLICKHOUSE_HOST', 'localhost'),
        port=int(os.getenv(f'{prefix}_CLICKHOUSE_PORT', 8123)),
        username=os.getenv(f'{prefix}_CLICKHOUSE_USER', 'admin'),
        password=os.getenv(f'{prefix}_CLICKHOUSE_PASS', 'pass4admin'),
        database=os.getenv(f'{prefix}_CLICKHOUSE_DB', 'default')
    )

    try:
        credentials.validate()
        logger.info(f"Successfully loaded ClickHouse credentials for '{env}' environment.")
    except ValueError as e:
        logger.error(f"Credential error for environment '{env}': {e}")
        raise

    return credentials