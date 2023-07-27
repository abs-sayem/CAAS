from tune_pdf import getText
from preprocess import cleanText

file = 'dataset/divai2020_benkova.pdf'
pdf_text = getText(file)
cleaned_text = cleanText(pdf_text)

print("Write your prompt here and hit enter. To exit from chat prompt 'bye'.\n")
user_input = input("User: ")
print(f"Bot : {cleaned_text[:500]}")