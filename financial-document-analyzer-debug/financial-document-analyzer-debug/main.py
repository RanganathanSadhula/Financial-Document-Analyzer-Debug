from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from typing import List, Optional
import PyPDF2

app = FastAPI(title="PDF Analyzer API")

# In-memory store for uploaded PDFs
pdf_text_store = {}

# ----------------------------
# Upload PDF and store text
# ----------------------------
@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    # Read PDF content
    reader = PyPDF2.PdfReader(file.file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    
    # Save in memory
    pdf_text_store[file.filename] = text
    
    return {"filename": file.filename, "text_length": len(text)}

# ----------------------------
# Analyze PDF for queries
# ----------------------------
@app.get("/analyze-pdf/{filename}")
async def analyze_pdf(filename: str, query: str):
    if filename not in pdf_text_store:
        raise HTTPException(status_code=404, detail="PDF not found")
    
    text = pdf_text_store[filename]
    
    # Split multiple queries by comma, remove quotes/spaces
    queries = [q.strip().strip('"').strip("'") for q in query.split(",") if q.strip()]
    
    results = {}
    for q in queries:
        # Find lines containing the query
        matches = [line for line in text.splitlines() if q.lower() in line.lower()]
        results[q] = matches
    
    return {
        "filename": filename,
        "query": queries,
        "results": results
    }

# ----------------------------
# Optional: Get full PDF text
# ----------------------------
@app.get("/get-pdf-text/{filename}")
async def get_pdf_text(filename: str):
    if filename not in pdf_text_store:
        raise HTTPException(status_code=404, detail="PDF not found")
    
    return {"filename": filename, "text": pdf_text_store[filename]}