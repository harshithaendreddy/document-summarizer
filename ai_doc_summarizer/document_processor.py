import google.generativeai as genai
import os
from PyPDF2 import PdfReader
from docx import Document
from nltk.tokenize import sent_tokenize

GENAI_API_KEY = ""  
genai.configure(api_key=GENAI_API_KEY)

# Load the AI model
model = genai.GenerativeModel("gemini-pro")  

def extract_text(filepath):
    """Extract text from different document types."""
    ext = os.path.splitext(filepath)[1].lower()

    if ext == ".pdf":
        return extract_text_from_pdf(filepath)
    elif ext == ".docx":
        return extract_text_from_docx(filepath)
    elif ext == ".txt":
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()
    else:
        return "Unsupported file format."

def extract_text_from_pdf(filepath):
    """Extract text from PDF."""
    text = ""
    with open(filepath, "rb") as file:
        pdf = PdfReader(file)
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip() if text.strip() else "No text found in the PDF."

def extract_text_from_docx(filepath):
    """Extract text from Word DOCX."""
    doc = Document(filepath)
    text = "\n".join([p.text for p in doc.paragraphs])
    return text.strip() if text.strip() else "No text found in the DOCX."

def summarize_text(text):
    """Summarize text using Gemini API."""
    if not text.strip():
        return "No text available for summarization."
    
    prompt = f"Summarize the following text in a concise and clear way:\n\n{text}"

    try:
        response = model.generate_content(prompt)
        return response.text  # Extract summarized text from Gemini API response
    except Exception as e:
        return f"Error in AI summarization: {str(e)}"
