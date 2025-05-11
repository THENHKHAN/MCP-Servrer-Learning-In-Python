from mcp.server.fastmcp import FastMCP

# Create an MCP server named "Demo"
mcp = FastMCP("Demo")

print("MCP Connected ...............")

# Define a tool for addition
@mcp.tool(description="Add two numbers together")
def add(a: int, b: int) -> int:
    """Adds two integers and returns the result."""
    return a + b

# Define a resource for personalized greetings
@mcp.resource("greeting://{name}", description="Get a personalized greeting by name")
def get_greeting(name: str) -> str:
    """Returns a greeting message for the given name."""
    return f"Hello, {name}!"

print("MCP Work done ...............")
