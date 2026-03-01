import os

from tavily import TavilyClient


def web_search(query):
    client = TavilyClient(os.getenv("TAVILY_API_KEY"))

    response = client.search(query, search_depth="basic", include_answer=True)

    return response.get("answer")


AVAILABLE_TOOLS = {
    "web_search": web_search,
}
