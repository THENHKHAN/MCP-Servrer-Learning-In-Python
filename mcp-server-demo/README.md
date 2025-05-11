# MCP Server with Inspector UI (Python)

## 📋 Prerequisites

Make sure the following are installed:

* Python 3.10+
* [uv](https://github.com/astral-sh/uv):

  ```bash
  pip install uv
  ```
* `mcp` SDK:

  ```bash
  uv pip install "mcp[cli]"
  ```
* Node.js, npm, and npx
* (Optional) [nvm-windows](https://github.com/coreybutler/nvm-windows) for managing Node versions

Verify versions:

```bash
node -v
npm -v
npx -v
```

---

## 📁 Project Structure

```
mcp-server-demo/
├── .venv/                  # Virtual environment
├── server.py               # Your MCP server code
└── pyproject.toml          # Optional, for dependencies
```

---

## 🧠 server.py

```python
from mcp.server.fastmcp import FastMCP

# Create an MCP server named "Demo"
mcp = FastMCP("Demo")

print("MCP Connected ...............")

# Tool: Add two integers
@mcp.tool(description="Add two numbers together")
def add(a: int, b: int) -> int:
    """Adds two integers and returns the result."""
    return a + b

# Resource: Greet by name
@mcp.resource("greeting://{name}", description="Get a personalized greeting by name")
def get_greeting(name: str) -> str:
    """Returns a greeting message for the given name."""
    return f"Hello, {name}!"

print("MCP Work done ...............")
```

---

## 🚀 Run the Server with Inspector UI

Activate the virtual environment:

```bash
.\.venv\Scripts\activate.bat  # Windows
# or
source .venv/bin/activate      # macOS/Linux
```

Run the dev server:

```bash
mcp dev server.py:mcp
```

Expected output:

```
MCP Connected ...............
MCP Work done ...............
```

> This launches the Inspector UI at [http://localhost:8080](http://localhost:8080)

---

## 🛠 Troubleshooting

### ❌ npx not found

Ensure `npx` is in your `PATH`. Temporarily fix with:

```cmd
SET PATH=C:\nvm4w\nodejs;%PATH%
```

Or add permanently via System Environment Variables.

### ❌ localhost refused to connect

Try launching the inspector manually:

```bash
npx @mcp/inspector
```

Or with a custom port:

```bash
npx @mcp/inspector --port 8081
```

---

## 🧪 Inspector Features

Visit [http://localhost:8080](http://localhost:8080):

* See your registered MCP server (`Demo`)
* Test tools like `add`
* Access resources like `greeting://{name}`
* Interact with inputs and view outputs

---

## ✅ Next Steps

* Add more tools with `@mcp.tool()`
* Add more resources with `@mcp.resource()`
* Scale with module-based code
* Connect to clients like Claude, Sora, etc.

---

Happy MCP building! 🚀
