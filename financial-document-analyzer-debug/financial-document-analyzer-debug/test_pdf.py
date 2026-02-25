# test_pdf.py
import asyncio
from tools import FinancialDocumentTool

pdf_path = r"C:\Users\gamin\Downloads\financial-document-analyzer-debug\financial-document-analyzer-debug\data\TSLA-Q2-2025-Update.pdf"  # your Tesla PDF

content = asyncio.run(FinancialDocumentTool.read_data_tool(path=pdf_path))
print("PDF Content Preview:")
print(content[:500])  # print first 500 chars