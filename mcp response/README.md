# Response Saver Python MCP Server

A Model Context Protocol (MCP) server that saves AI-generated responses directly to local Markdown files.

## Project Structure

```
response-mcp/
├── .python-version
├── pyproject.toml
├── README.md
└── main.py
```

## How to Run

### stdio Mode (Default)
```bash
uv run python main.py
```

### Dev Testing with MCP Inspector
```bash
uv run mcp dev main.py
```

## Saved Files Location
All generated responses are saved to: `~/mcp-responses/` (`C:\Users\vijen\mcp-responses\`).
