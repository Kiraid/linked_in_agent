import os
import requests
from dotenv import load_dotenv

load_dotenv()

# this function scrapes the linkedin profile infromation
# for now it is mocked, but in futire it will scrape from an API
def scrape_linked_profile(linked_profil_url: str, mock: bool = False):
    """ scrape information from linkedin profiles, 
    manually scrape the information from the linkedin profile"""
    
    if mock:
        linked_profil_url = "https://gist.githubusercontent.com/DanielaRosenn/42171e9c6bd97c70cc1f91bc7767eb91/raw/0b66b84048de507db1ce7a632a123ea98a378eb6/eden-marco-scrapin.json"
        response = requests.get(linked_profil_url, timeout=10)  
        return(response.json())
    else:
        print("Unable to get data")    


if __name__ == "__main__":
    print(
        scrape_linked_profile(
            linked_profil_url="https://www.linkedin.com/in/eden-marco",
            mock=True
        )
    )