# task.py
from crewai.agents import Agent
from crewai_tools import read_data_tool, search_tool

# Define the financial analyst agent
analyze_financial_document = Agent(
    name="financial_analyst",
    description="Analyze the financial document and summarize key points.",
    tools=[read_data_tool, search_tool],
    async_execution=False  # You can change to True if you want async
)