from langchain.serpapi import SerpAPIWrapper
from langchain.agents import tool


@tool
def get_profile_url(text: str) -> str:
    """ Searches for Linkedin Profile page url in text.

    :param text: The text to extract the url from.
    :return: The url of the LinkedIn profile.
    """
    search = SerpAPIWrapper()
    res = search.run(f"{text}")
    return res
