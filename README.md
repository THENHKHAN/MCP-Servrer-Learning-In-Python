# 🧠 MCP Server Learning in Python

## 📘 Overview

The **Model Context Protocol (MCP)** allows you to build servers that expose **data** and **functionality** to LLM (Large Language Model) applications in a **secure**, **modular**, and **standardized** way.

Think of it as a specialized **web API** tailored for LLMs.

### ✨ What MCP Servers Can Do:

- 🔍 **Resources**: Expose data (like `GET` endpoints) – used to load context into the LLM.
- 🛠️ **Tools**: Provide functionality (like `POST` endpoints) – used to run code or cause side effects.
- 💬 **Prompts**: Define reusable templates for interacting with LLMs.
- 📦 And much more!

---

## 🎯 Project Purpose

This repository is a **learning sandbox** for MCP servers, covering:
- 🚀 Basic starter examples
- 📁 Small to large projects
- 🔬 Experimentation with different MCP patterns

Whether you're new to MCP or want to build serious projects with it, this repo will grow alongside your understanding.

---

🧠 MCP Primitives
🗃️ Resources – Like read-only APIs (GET) for loading data into LLM context

🛠️ Tools – Like actions (POST) that trigger side effects

🧾 Prompts – Templated user interaction patterns

## 🧩 What is the MCP Python SDK?

The **Model Context Protocol (MCP) Python SDK** is the official tool for building structured, standardized interfaces between LLMs and external tools or data sources. It supports building both **servers** and **clients** that communicate using defined primitives.

---

## 🧠 Prerequisite Knowledge

This quickstart assumes you have familiarity with the following concepts:

- **Python**: Basic to intermediate knowledge of Python programming.
- **LLMs**: Familiarity with Large Language Models (LLMs) like Claude.

If you're not familiar with these technologies, we recommend reviewing relevant documentation or tutorials before proceeding.

---

## 💻 System Requirements

- Python **3.10 or higher**
- MCP Python SDK **v1.2.0 or higher**
- [`uv`](https://github.com/astral-sh/uv) – recommended for managing dependencies and virtual environments

---

## 🛠 Installing `uv`

[UV](https://github.com/astral-sh/uv) is a fast Python package and environment manager.

---
#### ✅ Windows (PowerShell):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# ✅ After install, verify versions:
python --version
uv --version
```

**Waring:** 'uv' is not recognized as an internal or external command...
then Edit the system environment variables and the uv path
```
C:\Users\<YourUsername>\.local\bin
```

## 🧰 Create Project

```bash
uv init mcp-server-demo
cd mcp-server-demo
uv add "mcp[cli]"
```

**This:** <br>
   * Initializes the project with pyproject.toml <br>
   * Creates a .venv folder <br>
   * Installs the MCP SDK and its CLI <br>

#### ✅ You can install this server in Claude Desktop and interact with it right away by running:
```
mcp install server.py
or
uv run mcp install <FilePath> ex: server.py
```
### Alternatively, you can test it with the MCP Inspector: Currenlty geeting error 
```
mcp dev server.py
```

## 🔁 Activate the Virtual Environment

To activate the virtual environment (in **Git Bash** or **PowerShell**):

```bash
source .venv/Scripts/activate
On  CMD: 
.\.venv\Scripts\activate.bat
```
* You should now see the prompt change to something like:
```bash
(mcp-server-demo) $
```

* To deactivate the environment, simply run:
```bash
 deactivate   
 same for bash and cmd 
 ```

#### ✅ To run the server and client as Inspector:
* Starter Code with two tools only: for you can read Readme.md inside the project `mcp-server-demo`
```python
from mcp.server.fastmcp import FastMCP

# Create an MCP server named "Demo"
mcp = FastMCP("Demo")

print("MCP Connected ...............")

# Define a tool for addition
@mcp.tool(description="Add two numbers together")
def add(a: int, b: int) -> int:
    """Adds two integers and returns the result."""
    return a + b


@mcp.tool(description="Subtracts two numbers together")
def difference(a: int, b: int) -> int:
    """Subtracts two integers and returns the result."""
    return a - b

# Define a resource for personalized greetings
@mcp.resource("greeting://{name}", description="Get a personalized greeting by name")
def get_greeting(name: str) -> str:
    """Returns a greeting message for the given name."""
    return f"Hello, {name}!"

print("MCP Work done ...............")
```
* Written a scripts that run the server :
   `runMcpServerViaInspectorCLient.bat`
```bash
   @echo off
echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo Ensuring npx is available in PATH...
set PATH=C:\nvm4w\nodejs;%PATH%

echo Starting MCP Dev Server...
mcp dev server.py:mcp

pause
```
