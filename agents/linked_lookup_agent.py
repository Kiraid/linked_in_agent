import os
from dotenv import load_dotenv 
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    AgentExecutor,
    create_react_agent,
)
from langchain import hub
from tools.tools import get_profile_url_tavily
load_dotenv()

# Given a username, function calls an llm with a tool that allows for browing the web
# to get the linkedin profile URL of the person
def lookup(name: str) -> str:
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
    template = """ Given the full name {name_of_person}, i want you to get me a link to their linkedin profile.
                        Your answer should only contain a url """
    
    prompt_template = PromptTemplate(template=template, input_variables=["name_of_person"])
    
    tools_for_agent = [
        Tool(
            name = "Crawl Google 4 Linkedin Profile",
            func = get_profile_url_tavily,
            description="Use for when you need to get the linkedin Page URL",
        )
    ]
    
    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)
    
    result = agent_executor.invoke(
        input = {"input": prompt_template.format(name_of_person=name)}
    )
    
    linked_profile_url = result["output"]
    return linked_profile_url
    
if __name__ == "__main__":
    linked_url = lookup(name="Eden Marco Udemy")