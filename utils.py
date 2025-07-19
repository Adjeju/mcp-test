from server import mcp
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
    description: str
    job: str


@mcp.tool()
def create_user(name: str) -> User:
    """Create a new user with the given name"""
    return User(name=name, age=20, description="A user", job="Engineer")
