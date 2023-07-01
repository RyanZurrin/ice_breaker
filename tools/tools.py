from langchain.utilities import SerpAPIWrapper


class CustomSerpAPIWrapper(SerpAPIWrapper):
    def __init__(self):
        super(CustomSerpAPIWrapper, self).__init__()

    @staticmethod
    def _process_response(res: dict) -> str:
        """Process response from SerpAPI."""
        if "error" in res:
            raise ValueError(f"Got error from SerpAPI: {res['error']}")
        if "answer_box" in res and "answer" in res["answer_box"].keys():
            return res["answer_box"]["answer"]
        elif "answer_box" in res and "snippet" in res["answer_box"].keys():
            return res["answer_box"]["snippet"]
        elif (
            "answer_box" in res
            and "snippet_highlighted_words" in res["answer_box"].keys()
        ):
            return res["answer_box"]["snippet_highlighted_words"][0]
        elif (
            "sports_results" in res
            and "game_spotlight" in res["sports_results"].keys()
        ):
            return res["sports_results"]["game_spotlight"]
        elif (
            "knowledge_graph" in res
            and "description" in res["knowledge_graph"].keys()
        ):
            return res["knowledge_graph"]["description"]
        elif "snippet" in res["organic_results"][0].keys():
            return res["organic_results"][0]["link"]

        else:
            return "No good search result found"


def get_profile_url(name: str):
    """Searches for Linkedin or twitter Profile Page."""
    search = CustomSerpAPIWrapper()
    return search.run(f"{name}")
