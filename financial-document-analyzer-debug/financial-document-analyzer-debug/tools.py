# tools.py
import os
from PyPDF2 import PdfReader
from crewai_tools import BaseTool, tools  # import BaseTool

search_tool = tools.search_tool  # legacy search tool

class FinancialDocumentTool:

    @staticmethod
    async def read_data(path=r'data/sample.pdf'):
        """Read a PDF and return text content"""
        if not os.path.exists(path):
            return "No file found at path."

        try:
            reader = PdfReader(path)
            full_text = ""
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    while "\n\n" in text:
                        text = text.replace("\n\n", "\n")
                    full_text += text + "\n"
            return full_text if full_text.strip() else "PDF text extraction returned no content."
        except Exception as e:
            return f"Error reading PDF: {str(e)}"

# Wrap async function in BaseTool for CrewAI
FinancialDocumentTool.read_data_tool = BaseTool(
    name="read_financial_pdf",
    description="Reads financial PDF and returns the text content",
    func=FinancialDocumentTool.read_data
)