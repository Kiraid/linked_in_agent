
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from third_parties.linkedin import scrape_linked_profile
from agents.linked_lookup_agent import lookup as linked_lookup_agent

# Calls the linked_lookup_agent with the given name to get Linkedin Profile URL
# Then scrapes the profile information and generates a summary and interesting facts about the person
def ice_break_with(name: str):
    linked_url = linked_lookup_agent(name=name)
    summary_template = """
    Given the linkedin information {information} about a person, i want you to create:
    1. a short summary of the person
    2. two intresting facts about the person
"""    

    summary_prompt_tempelate = PromptTemplate(input_variables=["information"], template=summary_template)

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
    chain = summary_prompt_tempelate | llm | StrOutputParser()
    linkedin_data = scrape_linked_profile(linked_profil_url=linked_url, mock=True)
    res = chain.invoke(input={"information": linkedin_data})
    print(res)
    

if __name__ == '__main__':
    print("Ice Breaker Enter") 
    load_dotenv()
    ice_break_with(name="Eden Marco Udemy")
