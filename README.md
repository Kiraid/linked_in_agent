# AI Agent – Profile Lookup & Summary

##  Description
This project implements an **AI Agent** that, given a specified username (and optionally a keyword), will:
1. **Search the internet** using an LLM-powered agent to find the matching profile URL.
2. If multiple similar usernames appear, **the first match** will be returned.  
   >  For better accuracy, include a keyword in your query that appears in the profile’s description.
3. **Scrape the found URL** to retrieve profile data.  
   *(Currently this uses a mock static file because LinkedIn’s API is paid and no free alternative was found.)*
4. **Generate a short summary** of the person.
5. **Provide two interesting facts** about them.

---

## Tech Stack
- **Python 3.12+**
- **LangChain** – for chaining LLM calls.
- **Google Gemini API** – as the LLM backend.
- **Tavily Search API** – for internet profile lookup.
- **Dotenv** – for environment variable management.

---

## Project Structure
.
├── agents/
│ └── linked_lookup_agent.py # AI Agent to search for profile URLs
├── third_parties/
│ └── linkedin.py # LinkedIn scraper (currently mock data)
├── tools/
│ └── tools.py # Tool functions (Tavily search wrapper)
├── iceBreaker.py # Main script for running the pipeline
├── Pipfile # Pipenv dependency file
├── Pipfile.lock # Locked dependencies
├── pycache/ # Python bytecode cache
└── README.md # This file
