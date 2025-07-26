from server import mcp

from utils import call_defra_docs

# Entry point to run the server
if __name__ == "__main__":
    mcp.run(
        transport="sse",
    )
