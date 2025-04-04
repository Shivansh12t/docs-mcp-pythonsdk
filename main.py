import os
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import json
import httpx
from bs4 import BeautifulSoup


mcp = FastMCP("docs")

load_dotenv()

serper_api_key = os.getenv("SERPER_API_KEY")

USER_AGENT = "docs-app/1.0"
SERPER_URL="https://google.serper.dev/search"

docs_urls = {
    "langchain": "python.langchain.com/docs",
    "llama-index": "docs.llamaindex.ai/en/stable",
    "openai":"platform.openai.com/docs",
}

async def search_web(query: str) -> dict | None:
    payload = json.dumps({"q":query, "nums": 2})

    headers = {
        "X-API-KEY": serper_api_key,
        "Content-Type": "application/json",
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                SERPER_URL, headers=headers, data=payload, timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except httpx.TimeoutException:
            return {"organic": []}

async def fetch_url(url: str) -> dict | None:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=30.0)
            soup = BeautifulSoup(response.text, "html.parser")
            text = soup.get_text()
            return text
        except httpx.TimeoutException:
            return "Timeout error"

@mcp.tool()
async def get_docs(query: str, library: str):
    """
    Search the docs for a given query and Library.
    Supports langchain, openai and llama-index.

    Args:
    query: the query to search for (e.g. "Chroma DB")
    library: The Library to search in (e.g. "langchain")

    Returns:
    Text from the documentation
    """
    if library not in docs_urls:
        raise ValueError(f"Library {library} not supported by this tool")
    query = f"site:{docs_urls[library]} {query}"
    results = await search_web(query)

    if len(results["organic"]) == 0:
        return "No Results Found"
    
    text = ""
    for result in results["organic"]:
        text += await fetch_url(result["link"])
    return text

def main():
    print("server is starting...")
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()