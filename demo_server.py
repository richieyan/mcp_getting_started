from mcp.server import FastMCP

# Create an MCP server
app = FastMCP("Demo")


# Add a tool, will be converted into JSON spec for function calling
@app.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Specific prompt templates for better use
@app.prompt()
def review_code(code: str) -> str:
    return f"Please review this code:\n\n{code}"


if __name__ == "__main__":
    app.run(transport='stdio')
