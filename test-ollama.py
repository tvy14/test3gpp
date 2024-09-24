import ollama
import requests
from pypdf import PdfReader

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = "\n".join([page.extract_text() for page in reader.pages])
    return text

def summarize_with_ollama(text, model="Mistral-nemo"):
    url = "http://localhost:8080/api/summarize"
    payload = {"text": text, "model": model}
    response = requests.post(url, json=payload)
    return response.json()["summary"]

#summary from ollama inference
pdf_text = extract_text_from_pdf(".pdf")
summary = summarize_with_ollama(pdf_text)
print(summary)
