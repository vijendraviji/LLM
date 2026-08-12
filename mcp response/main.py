from datetime import datetime
from pathlib import Path
from mcp.server import MCPServer

mcp = MCPServer("Response Saver")

OUTPUT_DIR = Path.home() / "mcp-responses"
OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

@mcp.tool()
def save_response(
    filename: str,
    content: str
) -> str:
    """
    Save an AI-generated response to a local Markdown file.
    Args:
        filename: Name of the file to create.
        content: Content to save into the file.
    """
    safe_filename = Path(filename).name
    if not safe_filename:
        raise ValueError("Invalid filename.")
    if not safe_filename.endswith(".md"):
        safe_filename += ".md"
    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    document = f"""# AI Response
**Generated:** {timestamp}

---

{content}
"""
    file_path = OUTPUT_DIR / safe_filename
    file_path.write_text(
        document,
        encoding="utf-8"
    )
    return f"Response saved successfully to: {file_path}"

if __name__ == "__main__":
    mcp.run()
