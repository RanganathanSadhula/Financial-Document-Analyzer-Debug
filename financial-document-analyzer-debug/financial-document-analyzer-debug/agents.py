from crewai_tools import read_data_tool, search_tool

class FinancialAnalyst:
    def __init__(self):
        self.tools = {
            "read_data": read_data_tool,
            "search": search_tool
        }

    async def analyze_pdf(self, path):
        return await self.tools["read_data"]._run(path)

    async def search_finance(self, query):
        return await self.tools["search"]._run(query)

financial_analyst = FinancialAnalyst()