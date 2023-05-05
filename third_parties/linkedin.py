import os
import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    """ Scrape information from a LinkedIn profiles.
    Manually scrape the information from a LinkedIn profile.

    :param linkedin_profile_url: The url of the LinkedIn profile.
    :return:  A dictionary of the scraped information.
    """
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": f'Bearer {os.environ["PROXYCURL_API_KEY"]}'}

    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    )

