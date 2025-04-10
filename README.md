# Documentation MCP Server with Python SDK

## Prerequisites
- `uv` package manager, (optional but **highly recommended**)
- claude desktop or cursor ( basically any MCP client )
- Serper Account - For Search Tool (free no Credit Card Required)

### Installation
Adding MCP to your Python Project
```shell
uv add "mcp[cli]"
```
Alternatively, for projects using pip for dependencies:
```shell
pip install "mcp[cli]"
```

## Developer-QuickStart
### Clone the Repository
```shell
git clone https://github.com/shivansh12t/docs-mcp-pythonsdk
cd docs-mcp-pythonsdk
```
### Install Dependencies (Optional)
```shell
uv pip sync
```
### Create a .env according to template.env
```
SERPER_API_KEY=<your_api_key>
```
### Add MCP Server to VSCode Copilot chat
1. go to `.vscode/mcp.json`
2. update the args to your absolute path to the mcp server
3. It should be up and running in `Agent Mode`
4. If you are having any issues, visit [Use MCP Servers in VSCode Copilot Chat](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_use-mcp-tools-in-agent-mode)

### Add MCP to Client - here Claude Desktop
1. Open Claude Desktop, go to settings `shift + ,`
2. `Edit Configurations`
3. add the following json with correct path to `claude_desktop_configurations.json`
```json
{
    "mcpServers": {
            "documentation": {
                "command": "uv",
                "args": [
                    "--directory",
                    "absolute/path/to/the/project",
                    "run",
                    "main.py"
                ]
            }
        }
}
```
4. Restart Claude & If you see a Hammer Sign near the Chatbox, Congrats your MCP is Up and Running

### Use MCP inspector
```shell
npx @modelcontextprotocol/inspector uv run main.py
```
