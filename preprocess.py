import nltk
import re
import string
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

def cleanText(text):

    #text = str(text).lower()
    #text = re.sub('\s', '', text)
    #text = re.sub('\[.*?\]', '', text)
    #text = re.sub('https?://\S+|www\.\S+', '', text)
    #text = re.sub('<.*?>+', '', text)
    #text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\t', ' ', text)
    text = re.sub('\n', ' ', text)
    #text = re.sub("\(cid:\d{1,2}\)", "", text)
    #text = re.sub('\W', ' ', text)
    #text = re.sub(' {2}', ' ', text)

    return(text)

def preprocessInput(string):
    u_input = str(string).lower()
    u_input = re.sub('\t', ' ', u_input)
    u_input = re.sub('\n', ' ', u_input)
    u_input = ["".join(word) for word in u_input.split(' ') if word not in stop_words]
    return(u_input)