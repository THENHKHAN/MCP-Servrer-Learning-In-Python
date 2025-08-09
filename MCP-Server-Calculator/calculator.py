# basic import 
from mcp.server.fastmcp import FastMCP
import math


# instantiate an MCP server client
mcp = FastMCP("Hello Calculator")

print("FastMCP calculator module loaded")


# DEFINE TOOLS

#addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return int(a + b)

# subtraction tool
@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    return int(a - b)

# multiplication tool
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return int(a * b)

#  division tool
@mcp.tool() 
def divide(a: int, b: int) -> float:
    """Divide two numbers"""
    return float(a / b)

# DEFINE RESOURCES

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


 # execute and return the stdio output
if __name__ == "__main__":
    print("Starting interactive MCP run...")
    mcp.run(transport="stdio")
    print("This should not print unless run() exits.")


# if __name__ == "__main__":
#     print("Starting interactive MCP run...")
#     mcp.run()
#     print("This should not print unless run() exits.")