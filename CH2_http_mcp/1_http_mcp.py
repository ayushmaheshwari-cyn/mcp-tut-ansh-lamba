from fastmcp import FastMCP 

#create an instance of the FastMCP class
mcp = FastMCP()

@mcp.tool()
async def fetch_http(): 
    """Use this tool to fetch data from a source"""

    #simulate fetching data from a source
    """You can make some API calls or database queries here to fetch data from a database"""
    return {"data": "Hello, MCP!"}


@mcp.tool()
async def process_http(path: str):
    """Use this tool to process the fetched data"""

    #simulate processing the fetched data
    """You can perform some data processing or transformation here"""
    return {"processed_data": "Hello, MCP! This data has been processed at path: " + path}


if __name__ == "__main__":
    #run the MCP server using HTTP transport
    mcp.run(transport="streamable-http", host="0.0.0.0", port=8050)
