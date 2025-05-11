@echo off
echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo Ensuring npx is available in PATH...
set PATH=C:\nvm4w\nodejs;%PATH%

echo Starting MCP Dev Server...
mcp dev server.py:mcp

pause
