#!/usr/bin/env python3
"""
Test script to verify MCP server functionality
"""
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def test_mcp_server():
    """Test the MCP server functionality"""
    server_params = StdioServerParameters(command="python", args=["main.py"], env=None)

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the session
            await session.initialize()

            # List available tools
            tools = await session.list_tools()
            print("Available tools:")
            for tool in tools.tools:
                print(f"  - {tool.name}: {tool.description}")

            # Test the create_user tool
            if tools.tools:
                result = await session.call_tool("create_user", {"name": "TestUser"})
                print(f"\nTool result: {result}")


if __name__ == "__main__":
    asyncio.run(test_mcp_server())
