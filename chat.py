from tune_pdf import getText
from preprocess import cleanText

file = 'dataset/divai2020_benkova.pdf'
pdf_text = getText(file)
cleaned_text = cleanText(pdf_text)

print("Write your prompt here and hit enter. To exit from chat prompt 'bye'.\n")
user_input = input("User: ")
print(f"Bot : {cleaned_text[:500]}")

#-------------------------------------------------------------------------------------
# importing modules
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import load_model
import json
import random


# loading trained model
demobot1 = load_model("DemoBot1_10K")

# importing training data
training_data = pd.read_csv("dataset/training_data1.csv")

# importing responses
responses = json.load(open("dataset/responses1.json", "r"))
#print(responses)

# fitting TfIdfVectorizer with training data to preprocess inputs
training_data["patterns"] = training_data["patterns"].str.lower()
vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words="english")
vectorizer.fit(training_data["patterns"])

# fitting LabelEncoder with target variable(tags) for inverse transformation of predictions
le = LabelEncoder()
le.fit(training_data["tags"])

# preprocessing input
def predict_tag(inp_str):
    inp_data_tfidf = vectorizer.transform([inp_str.lower()]).toarray()
    predicted_proba = demobot1.predict(inp_data_tfidf)
    encoded_label = [np.argmax(predicted_proba)]
    predicted_tag = le.inverse_transform(encoded_label)[0]
    return predicted_tag

# Chat
print("---------------  DemoBot1_10K - AI Chat bot  ---------------")
print("Ask any queries regarding SASTRA...")
print("I will try to understand you and reply...")
print("Type Bye to quit...")
while True:
    user_input = input("\nAsk anything....: ")
    if user_input.lower() == "bye":
        break
    elif(user_input not in 'grettings'):
        if user_input:
            tag = predict_tag(user_input)
            response = random.choice(responses[tag])
            print("Response........:", response)
        else:
            pass
    else:
        if user_input.lower() == "":
            pass