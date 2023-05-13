<<<<<<< HEAD
from langchain.serpapi import SerpAPIWrapper
=======
from langchain.utilities import SerpAPIWrapper
>>>>>>> 62eddbc4decbe6ceadc065660d083486c96b79ba


class CustomSerpAPIWrapper(SerpAPIWrapper):
    def __init__(self):
        super(CustomSerpAPIWrapper, self).__init__()

    @staticmethod
    def _process_response(res: dict) -> str:
<<<<<<< HEAD
        """ Process the response from the SerpAPI.

        :param res: The response from the SerpAPI.
        :return: The url of the LinkedIn profile.
        """
=======
        """Process response from SerpAPI."""
>>>>>>> 62eddbc4decbe6ceadc065660d083486c96b79ba
        if "error" in res.keys():
            raise ValueError(f"Got error from SerpAPI: {res['error']}")
        if "answer_box" in res.keys() and "answer" in res["answer_box"].keys():
            toret = res["answer_box"]["answer"]
        elif "answer_box" in res.keys() and "snippet" in res["answer_box"].keys():
            toret = res["answer_box"]["snippet"]
        elif (
<<<<<<< HEAD
                "answer_box" in res.keys()
                and "snippen_highlighted_words" in res["answer_box"].keys()
        ):
            toret = res["answer_box"]["snippet_highlighted_words"][0]
        elif (
                "sports_results" in res.keys()
                and "game_spotlight" in res["sports_results"].keys()
        ):
            toret = res["sports_results"]["game_spotlight"]
        elif (
                "knowledge_graph" in res.keys()
                and "description" in res["knowledge_graph"].keys()
=======
            "answer_box" in res.keys()
            and "snippet_highlighted_words" in res["answer_box"].keys()
        ):
            toret = res["answer_box"]["snippet_highlighted_words"][0]
        elif (
            "sports_results" in res.keys()
            and "game_spotlight" in res["sports_results"].keys()
        ):
            toret = res["sports_results"]["game_spotlight"]
        elif (
            "knowledge_graph" in res.keys()
            and "description" in res["knowledge_graph"].keys()
>>>>>>> 62eddbc4decbe6ceadc065660d083486c96b79ba
        ):
            toret = res["knowledge_graph"]["description"]
        elif "snippet" in res["organic_results"][0].keys():
            toret = res["organic_results"][0]["link"]
<<<<<<< HEAD
=======

>>>>>>> 62eddbc4decbe6ceadc065660d083486c96b79ba
        else:
            toret = "No good search result found"
        return toret


<<<<<<< HEAD
def get_profile_url(text: str) -> str:
    """ Searches for Linkedin Profile page url in text.

    :param text: The text to extract the url from.
    :return: The url of the LinkedIn profile.
    """
    search = CustomSerpAPIWrapper()
    res = search.run(f"{text}")
=======
def get_profile_url(name: str):
    """Searches for Linkedin or twitter Profile Page."""
    search = CustomSerpAPIWrapper()
    res = search.run(f"{name}")
>>>>>>> 62eddbc4decbe6ceadc065660d083486c96b79ba
    return res
