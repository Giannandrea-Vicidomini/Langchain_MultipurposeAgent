import os
import requests
from langchain_core.tools import tool
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())


@tool
def search_youtube_tool(query_string: str) -> list[str]:
    """
    This function should be used when you want to search for youtube videos based on the query string,
    it can be a topic or something along those lines
    args:
        query_string: the string used to search youtube
    """
    base_url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "key": os.getenv("YOUTUBE_API_KEY"),
        "q": query_string,
        "part": "snippet",
        "max_result": 20,
    }
    result = requests.get(base_url, params=params)
    if result.status_code == 200:
        return [item["snippet"]["title"] for item in result.json()["items"]]
    else:
        return []
