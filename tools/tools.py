from langchain_tavily import TavilySearch
import os
from dotenv import load_dotenv
load_dotenv()
def get_profile_url_tavily(name: str):
    """Searches for LinkedIn or Twitter profile page."""
    search = TavilySearch(api_key=os.getenv("TAVILY_API_KEY"))
    results = search.run(f"{name}")
    return results
