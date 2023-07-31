from pdfminer.high_level import extract_text
from preprocess import cleanText

def getPdfText(file):
    pdf_file_text = extract_text(file)
    cleaned_text = cleaned_text(pdf_file_text)
    return(pdf_file_text)
