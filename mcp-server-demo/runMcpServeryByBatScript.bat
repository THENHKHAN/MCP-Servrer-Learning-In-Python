@echo off
REM Change directory to your project folder
cd /d F:\McpServerLearning10may25\MCP-Servrer-Learning-In-Python\mcp-server-demo

REM Run the server with correct MCP object path
uv run --with mcp[cli] mcp run server.py:mcp
pause
