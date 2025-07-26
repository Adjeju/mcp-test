from config import config, Config
from contextlib import asynccontextmanager
from typing import Optional, List
import asyncpg
import asyncio


class DatabaseError(Exception):
    """Custom database exception"""

    pass


class DatabaseManager:
    """Enhanced async PostgreSQL manager using asyncpg with connection pooling and advanced features"""

    def __init__(self, config: Config):
        self.config = config
        self.pool: Optional[asyncpg.Pool] = None
        self._is_connected = False
        self._retry_attempts = 3
        self._retry_delay = 1.0

    async def create_pool(self) -> None:
        """Create connection pool with retry logic"""
        if not self.config.DATABASE_URL:
            raise ValueError("Database URL not configured")

        for attempt in range(self._retry_attempts):
            try:
                print(
                    f"Attempting to create database pool (attempt {attempt + 1}/{self._retry_attempts})"
                )

                self.pool = await asyncpg.create_pool(
                    self.config.DATABASE_URL,
                    min_size=5,
                    max_size=20,
                    max_queries=50000,
                    max_inactive_connection_lifetime=300.0,
                    command_timeout=60,
                    server_settings={
                        "jit": "off"  # Disable JIT for better performance in some cases
                    },
                )

                # Test the connection
                await self.health_check()
                self._is_connected = True
                print("✅ Database connection pool created successfully")
                return

            except Exception as e:
                print(f"❌ Failed to create database pool (attempt {attempt + 1}): {e}")
                if attempt < self._retry_attempts - 1:
                    await asyncio.sleep(
                        self._retry_delay * (2**attempt)
                    )  # Exponential backoff
                else:
                    raise DatabaseError(
                        f"Failed to establish database connection after {self._retry_attempts} attempts: {e}"
                    )

    async def close_pool(self) -> None:
        """Close connection pool gracefully"""
        if self.pool:
            print("Closing database connection pool...")
            await self.pool.close()
            self._is_connected = False
            print("✅ Database connection pool closed")

    async def health_check(self) -> bool:
        """Check if database connection is healthy"""
        try:
            async with self.get_connection() as conn:
                result = await conn.fetchval("SELECT 1")
                return result == 1
        except Exception as e:
            print(f"Database health check failed: {e}")
            return False

    @property
    def is_connected(self) -> bool:
        """Check if database is connected"""
        return self._is_connected and self.pool is not None

    @asynccontextmanager
    async def get_connection(self):
        """Get a database connection from the pool"""
        if not self.pool:
            raise DatabaseError(
                "Database pool not initialized. Call create_pool() first."
            )

        try:
            async with self.pool.acquire() as connection:
                yield connection
        except Exception as e:
            print(f"Error acquiring database connection: {e}")
            raise DatabaseError(f"Failed to acquire database connection: {e}")

    @asynccontextmanager
    async def transaction(self):
        """Context manager for database transactions"""
        async with self.get_connection() as conn:
            async with conn.transaction():
                yield conn

    async def execute_query(self, query: str, *args) -> List[asyncpg.Record]:
        """Execute a query and return all results"""
        try:
            async with self.get_connection() as conn:
                print(f"Executing query: {query[:100]}...")
                return await conn.fetch(query, *args)
        except Exception as e:
            print(f"Query execution failed: {e}")
            raise DatabaseError(f"Query execution failed: {e}")

    async def __aenter__(self):
        """Async context manager entry"""
        await self.create_pool()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit"""
        await self.close_pool()
