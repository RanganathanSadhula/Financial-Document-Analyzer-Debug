# crewai_tools.py
from crewai.tools import BaseTool
import os
from PyPDF2 import PdfReader

# Tool to read PDF content
class ReadDataTool(BaseTool):
    name: str = "read_data_tool"
    description: str = "Reads PDF content and returns text"

    async def _run(self, path: str = "data/sample.pdf"):
        if not os.path.exists(path):
            return "File not found."
        reader = PdfReader(path)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text

read_data_tool = ReadDataTool()

# Dummy search tool
class SearchTool(BaseTool):
    name: str = "search_tool"
    description: str = "Search tool for financial queries"

    async def _run(self, query: str):
        # Replace this with real search logic if needed
        return f"Search result for query: {query}"

search_tool = SearchTool()