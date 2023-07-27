from pdfminer.high_level import extract_text

def getText(file):
    pdf_file_text = extract_text(file)
    return(pdf_file_text)