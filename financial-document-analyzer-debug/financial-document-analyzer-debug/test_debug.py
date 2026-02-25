# test_debug.py
import asyncio
from tools import FinancialDocumentTool, search_tool
from agents import financial_analyst

print("Testing search_tool:")
print(search_tool("Revenue analysis"))

print("\nTesting FinancialDocumentTool:")
doc_content = asyncio.run(FinancialDocumentTool.read_data_tool())
print(doc_content[:500])

print("\nTesting financial_analyst agent's tool:")
agent_tool = financial_analyst.tools[0]
agent_result = asyncio.run(agent_tool())
print(agent_result[:500])