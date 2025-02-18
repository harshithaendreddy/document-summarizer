# AI Document Summarizer

## Overview
The **AI Document Summarizer** is a web application that allows users to upload text documents (PDF, DOCX, TXT) and receive a concise summary using AI-powered text processing. The application is built with **Flask**, utilizes **NLTK** for text processing, and integrates with **Gemini AI** for advanced summarization.

## Features
- Upload documents in **PDF, DOCX, or TXT** format.
- Extracts and summarizes text from the document.
- Uses AI to generate an improved summary.
- Simple and interactive web interface.

## Tech Stack
- **Backend:** Flask
- **AI Summarization:** Google Gemini API
- **Text Processing:** NLTK
- **Frontend:** HTML, CSS (Jinja Templates)

## Installation & Setup

### 1. Clone the Repository
```sh
git clone https://github.com/harshithaendreddy/document-summarizer.git
cd document-summarizer
```

### 2. Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Set Up Google Gemini API (If AI Summarization is Used)
- Obtain an API key from Google Gemini.
- Create a `.env` file in the project root and add:
```sh
GEMINI_API_KEY=your_api_key_here
```

### 5. Run the Flask Application
```sh
python app.py
```

The application will be accessible at `http://127.0.0.1:5000/`.

## Project Structure
```
├── ai_doc_summarizer/
│   ├── app.py  # Flask App
│   ├── document_processor.py  # Handles text extraction & summarization
│   ├── templates/
│   │   ├── index.html  # Frontend UI
│   ├── uploaded_docs/  # Stores uploaded files
│   ├── static/  # CSS, JS files
│   ├── requirements.txt  # Dependencies
│   ├── .gitignore  # Ignoring unnecessary files
└── README.md
```

## Handling Large Files Issue in Git
To avoid pushing large files (like `venv/`, PyTorch libraries, etc.), ensure:
- `.gitignore` includes:
```
venv/
__pycache__/
uploaded_docs/
*.dll
*.lib
```
- If you mistakenly added large files, remove them:
```sh
git rm --cached -r venv/
git commit -m "Removed large files from tracking"
git push origin main
```
- If large files are necessary, use **Git LFS**:
```sh
git lfs install
git lfs track "*.dll"
git add .gitattributes
git commit -m "Enable Git LFS"
git push origin main
```

## Future Enhancements
- Deploy the application on **Render/AWS/GCP**.
- Improve summarization accuracy with **fine-tuned AI models**.
- Add support for multiple languages.

## Contributing
Feel free to fork the repo, create a branch, and submit a pull request. Any contributions to improve the AI summarization feature are welcome!

## License
MIT License. See `LICENSE` for details.

---
🚀 **Developed by Harshitha Reddy**

