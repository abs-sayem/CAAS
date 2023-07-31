# Greeting----------------------
from greetings import greet

# Pdf file tuning--------------------
from pdf_tune import getPdfText, getInfoFromPdf
from preprocess import preprocessInput

file = 'dataset/divai2020_benkova.pdf'
pdf_text = getPdfText(file)

#-------------------------------------------------------------------------------------
# importing modules
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import load_model
import json
import random
import warnings
warnings.filterwarnings("ignore")


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
print("---------------  DemoBot: AI Chat Bot  ---------------")
print("Ask any queries...\nI will try to understand you and reply...\nType 'Bye' to quit.")

while True:
    user_input = input("\nUser: ")
    if user_input.lower() == "bye":
        print("Bot : Good Bye. Have a nice day.")
        break
    else:
        # Check greetings
        if(greet(user_input.lower())!=None):
            print("Bot : " + greet(user_input) + "\n")
        elif(getInfoFromPdf(pdf_text, user_input)!= None):
            print("Bot : " + getInfoFromPdf(pdf_text, user_input) + "\n")
        elif user_input:
            tag = predict_tag(user_input)
            response = random.choice(responses[tag])
            print("Bot : ", response)
        elif user_input:
            pass