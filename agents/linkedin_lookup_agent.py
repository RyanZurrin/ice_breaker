from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI

from langchain.agents import initialize_agent, Tool, AgentType
from tools.tools import get_profile_url


def lookup(name: str) -> str:
    """ Lookup a person's LinkedIn url from their name.

    :param name: The name of the person to lookup.
    :return: A summary of the person's LinkedIn profile.
    """
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template = """
    given the full name {name_of_person} I want you to get it me a link to their 
    linkedin profile page. Your answer should contain only a url.
    """

    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url,
            description="useful for when you need to get a linkedin Page URL from a person's name",
        )
    ]

    agent = initialize_agent(
        tools_for_agent=tools_for_agent,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )
    linkedin_url = agent.run(prompt_template.format_prompt(name_of_person=name))
    return linkedin_url
