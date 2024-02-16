import os
import requests

def scrape_linkedin_profile():
    """scrape information from LinkedIn profiles,
    Manually scrape the inforamtion from the LinkedIn profile
    """
    json = requests.get("https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json").text
    return json
    pass