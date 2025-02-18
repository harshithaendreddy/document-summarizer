# Document Summarizer

This is a Flask-based web application that allows users to upload text documents and receive AI-generated summaries using Google's Gemini API.

## Features
- Upload `.txt`, `.docx`, and `.pdf` files for processing.
- Extract text from uploaded documents.
- Generate AI-powered summaries using the Gemini API.
- View and download the summarized text.

## Installation

### Prerequisites
Make sure you have the following installed:
- Python 3.8+
- pip

### Clone the Repository
```bash
git clone [<your-repo-url>](https://github.com/harshithaendreddy/document-summarizer.git)
cd document-summarizer
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Start the Flask Server
```bash
python app.py
```
The application will run at `http://127.0.0.1:5000/`.

### Upload and Summarize a Document
1. Open your browser and go to `http://127.0.0.1:5000/`
2. Click on "Upload File" and select a document.
3. Wait for the AI to process and display the summary.

### Download the Summary
Once the summary is generated, you can download the summarized text.

## Folder Structure
```
project-root/
│── app.py                  # Main Flask application
│── document_processor.py    # Handles text extraction and AI processing
│── templates/               # HTML templates
│── static/                  # Static assets (CSS, JS)
│── uploads/                 # Temporary file storage
│── requirements.txt         # Python dependencies
│── .env                     # Environment variables (not included in repo)
│── README.md                # Project documentation
```


