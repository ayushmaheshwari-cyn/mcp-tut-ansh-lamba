
from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()

async def main():

    tavily_api_key = os.getenv("TAVILY_API_KEY")

    if not tavily_api_key:
        raise ValueError("TAVILY_API_KEY not found in .env")

    client = MultiServerMCPClient(
        {
            "tavily": {
                "transport": "streamable-http",
                "url": (
                    "https://mcp.tavily.com/mcp/"
                    f"?tavilyApiKey={tavily_api_key}"
                ),
            }
        }
    )

    print("Connecting to Tavily MCP...")

    tools = await client.get_tools()

    print("\nAvailable Tavily MCP tools:\n")

    for tool in tools:
        print(f"Tool name: {tool.name}")
        print(f"Description: {tool.description}")
        print("-" * 50)

    print("\nTotal tools available:", len(tools))
    print("-" * 50)
    print("-" * 50)
    tool_search = [tool for tool in tools if tool.name == "tavily_search"][0]
    result = await tool_search.ainvoke({"query": "What is the capital of France?"})
    print("\nResult from Tavily search tool:", result)



if __name__ == "__main__":
    asyncio.run(main())
