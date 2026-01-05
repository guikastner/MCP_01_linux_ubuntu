"""Simple FastMCP server exposing a hello-world tool.

The server is intentionally minimal so it can run on a plain Ubuntu host.
"""
from __future__ import annotations

import platform
from datetime import datetime
import sys
from fastmcp import FastMCP

mcp = FastMCP("Ubuntu Hello MCP")


@mcp.tool
def hello(name: str = "world") -> str:
    """Return a friendly greeting with host information."""
    distro = platform.platform()
    hostname = platform.node()
    return f"Hello, {name}! This server is running on {hostname} ({distro})."


@mcp.resource(
    "resource://about/hello",
    name="Hello tool docs",
    description="Como usar a ferramenta hello",
    mime_type="text/plain",
)
def hello_resource() -> str:
    """Plain-text instructions for the hello tool."""
    return (
        "Tool: hello(name='world') -> str\n"
        "- Retorna uma saudação com informações do host.\n"
        "- Use sem argumento para obter o hello padrão; use hello('Maria') para personalizar."
    )


@mcp.resource(
    "resource://system/overview",
    name="System overview",
    description="Informações rápidas da máquina e do Python",
    mime_type="application/json",
)
def system_overview() -> dict:
    """Expose basic host and runtime information as JSON."""
    return {
        "hostname": platform.node(),
        "platform": platform.platform(),
        "python_version": sys.version.split()[0],
        "timestamp_utc": datetime.utcnow().isoformat() + "Z",
    }


if __name__ == "__main__":
    mcp.run()
