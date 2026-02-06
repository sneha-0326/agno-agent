from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

# load the env variables
load_dotenv()

llm = Groq(id="llama-3.3-70b-versatile", temperature=0)

# Initialize the agent with Groq provided LLM
agent = Agent(
    model=llm,
    description="You are a diligent research assistant skilled at gathering, analyzing and "
                "summarizing information form multiple sources",
    tools=[DuckDuckGoTools()],
    markdown=True,
)

# prompt the agent to perform a research task
agent.print_response(
    "Research the impact of AI on scientific discovery. Provide a summary with references"
)
