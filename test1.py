# importing modules
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import load_model
import json


# loading trained model
demobot1 = load_model("DemoBot1_10K")

# importing training data
training_data = pd.read_csv("dataset/training_data1.csv")

# importing responses
responses = json.load(open("dataset/responses1.json", "r"))

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
    inp = input("\nAsk anything... : ")
    if inp == "Bye" or "bye":
        break
    else:
        if inp:
            tag = predict_tag(inp)
            response = random.choice(responses[tag])
            print("Response........ : ", response)
        else:
            pass