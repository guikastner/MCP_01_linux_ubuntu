"""Simple FastMCP server exposing a hello-world tool.

The server is intentionally minimal so it can run on a plain Ubuntu host.
"""
from __future__ import annotations

import platform
from fastmcp import FastMCP

mcp = FastMCP("Ubuntu Hello MCP")


@mcp.tool
def hello(name: str = "world") -> str:
    """Return a friendly greeting with host information."""
    distro = platform.platform()
    hostname = platform.node()
    return f"Hello, {name}! This server is running on {hostname} ({distro})."


if __name__ == "__main__":
    mcp.run()
