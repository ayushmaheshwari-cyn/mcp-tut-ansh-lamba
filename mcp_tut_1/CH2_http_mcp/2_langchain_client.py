
from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio
import os

# Current script directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Project root directory
project_root = os.path.dirname(current_dir)

# MCP server script
mcp_server_script = os.path.join(
    project_root, "CH1_create_mcp/",
    "1_first_mcp_server_stdio.py"
)

# Virtual environment
venv_path = os.path.join(project_root, ".venv")

# Python executable
python_executable = os.path.join(
    venv_path,
    "Scripts",
    "python.exe"
)

async def main():

    # Verify paths
    print("Python executable:", python_executable)
    print("Python exists:", os.path.isfile(python_executable))

    print("MCP server script:", mcp_server_script)
    print("Server script exists:", os.path.isfile(mcp_server_script))

    # Create MCP client
    client = MultiServerMCPClient(
        {
            "data_fetch_mcp_stdio": {                             #mcp server 1
                "transport": "stdio",
                "command": python_executable,
                "args": [mcp_server_script],
            },
            "data_fetch_mcp_http": {                             #mcp server 2
                "transport": "streamable-http",
                "url": "http://localhost:8050/mcp"
            }
}
    )

    # Get available tools
    tools = await client.get_tools()
    print()
    print(tools)
    print()
    print("\nAvailable tools:")

    for tool in tools:
        print("Tool name:", tool.name)
        print("Description:", tool.description)


if __name__ == "__main__":
    asyncio.run(main())
