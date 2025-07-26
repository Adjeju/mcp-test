from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from dataclasses import dataclass
from mcp.server.fastmcp import FastMCP
from db import DatabaseManager
from config import config


@dataclass
class AppContext:
    db: DatabaseManager


@asynccontextmanager
async def lifespan(app: FastMCP) -> AsyncGenerator[AppContext]:
    db = DatabaseManager(config)
    await db.create_pool()
    try:
        yield AppContext(db=db)
    finally:
        await db.close_pool()


mcp = FastMCP("My App", sse=True, lifespan=lifespan)
