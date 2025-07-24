
import os
import pytesseract
from pdf2image import convert_from_path

def extract_text_from_file(file_path):
    if file_path.endswith(".txt"):
        with open(file_path, "r", encoding='utf-8') as f:
            return f.read()
    elif file_path.endswith(".pdf"):
        images = convert_from_path(file_path)
        text = ""
        for img in images:
            text += pytesseract.image_to_string(img)
        return text
    return ""
