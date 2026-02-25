>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Financial Document Analyzer - Debug Assessment ------------------------------------

******************************** Server runs at: http://127.0.0.1:8000/docs ****************************************


financial-document-analyzer-debug/
│
├── data/                 # sample PDF files
├── outputs/              # results of analysis
├── __pycache__/          # optional, can remove
├── agents.py
├── crewai_tools.py
# ├── main.py
├── task.py
├── tools.py
├── test_debug.py
├── test_env.py
├── test_pdf.py
├── requirements.txt
├── .env                  # config variables
└── README.md


# 1. >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>           Overview

The Financial Document Analyzer is an AI-powered system built to process corporate reports, financial statements, and investment documents.
This assessment focuses on debugging and optimizing the system to make it fully functional, accurate, and user-friendly.

Purpose of this assessment:

Identify and fix deterministic bugs in the code

Optimize AI prompts for better performance

Ensure smooth PDF processing and analysis

Deliver actionable financial insights

# 2. >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>    Project Workflow

Upload a financial document (PDF)

Extract text from the document

Run AI-powered analysis

Key financial metrics

Risk assessment

Investment recommendations

Market insights

Store or display analysis results

# 3. >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>     What I Did
# Step 1: Environment Setup

Installed dependencies: pip install -r requirements.txt

Configured .env for API keys and paths

Verified environment with test_env.py

# Step 2: Upload and Test PDFs

Added sample financial PDF (data/sample.pdf)

Ran test_pdf.py to ensure text extraction works correctly

# Step 3: Identified Bugs

During review, the following issues were found:

File: agents.py

Bug: Incorrect method calls to AI agent

Fix: Corrected function signatures and imported proper modules

File: tools.py

Bug: File path errors when reading PDFs

Fix: Added safe path handling and checks for file existence

File: crewai_tools.py

Bug: Inefficient AI prompts leading to low accuracy

Fix: Optimized prompts with clear instructions for financial context

File: main.py

Bug: API endpoints not returning proper JSON

Fix: Added proper response formatting and exception handling

File: task.py

Bug: Tasks were not executed sequentially

Fix: Implemented proper workflow with logging and error handling

# Step 4: Debug and Test

Ran test_debug.py for unit testing of modules

Ensured all API endpoints are functional

Verified AI analysis outputs accurate key metrics and recommendations

# 4. >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>     How to Run the Project
1. Start API Server

Run the command:

uvicorn main:app --reload

Server runs at: http://127.0.0.1:8000/docs

2. Upload a PDF

Endpoint: POST /upload-pdf

Parameter: PDF file

Response: Confirmation of upload

3. Extract Text from PDF

Endpoint: GET /get-pdf-text/{filename}

Example:

curl -X GET "http://127.0.0.1:8000/docs/get-pdf-text/sample.pdf"
4. Run Financial Analysis

Endpoint: POST /analyze

Parameter: Uploaded PDF filename

Response:

{
  "company": "Tesla",
  "period": "Q2 2025",
  "metrics": {
    "revenue": "...",
    "profit": "...",
    "risk_score": "..."
  },
  "recommendation": "Buy/Hold/Sell",
  "market_insights": "..."
}
5. View Output Files

Analysis results are saved in the outputs/ folder for further use

# 5. >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>    Final Results

Fully functional system with bug-free PDF upload, extraction, and analysis

Optimized AI prompts for accurate financial insights

API endpoints tested and returning structured JSON

Ready for submission and demonstration

# 6. >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>          Optional Enhancements

Concurrent request handling using Redis Queue / Celery

Database integration for storing documents and analysis results


# 7. >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>          Contact

For questions or feedback, contact: ranganathansadhula77@gmail.com