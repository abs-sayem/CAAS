from pdfminer.high_level import extract_text
from preprocess import cleanText
# For Feature Extruction
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk, string
import warnings
warnings.filterwarnings("ignore")

# Define the text extraction function
def lemTokens(tokens):
    lemmer = nltk.stem.WordNetLemmatizer()  # Removes the punctuation also lemmatize
    return([lemmer.lemmatize(token) for token in tokens])
def lemNormalize(text):
    remove_punkt_dict = dict((ord(punkt), None) for punkt in string.punctuation)
    return(lemTokens(nltk.word_tokenize(text.lower().translate(remove_punkt_dict))))

def createResponseFromText(sentence_tokens):
  bot_response = ""
  tfidfVec = TfidfVectorizer(tokenizer=lemNormalize, stop_words='english')
  tfidf = tfidfVec.fit_transform(sentence_tokens)
  values = cosine_similarity(tfidf[-1], tfidf)
  index = values.argsort()[0][-2]
  flat = values.flatten()
  flat.sort()
  req_tfidf = flat[-2]
  if(req_tfidf != 0):
    #bot_response = bot_response + "I'm sorry! I don't understand."
    #return bot_response
    #continue
  #else:
    bot_response = bot_response + sentence_tokens[index]
    return bot_response

def getPdfText(file):
    pdf_file_text = extract_text(file)
    cleaned_text = cleanText(pdf_file_text)
    return(cleaned_text)

def getInfoFromPdf(pdf_text, user_input):
    sent_tokens = nltk.sent_tokenize(pdf_text)
    word_tokens = nltk.word_tokenize(pdf_text)
    
    sent_tokens.append(user_input)
    #print("Bot : ", end="")
    warnings.filterwarnings("ignore")
    val = createResponseFromText(sent_tokens)
    return(val)
    sent_tokens.remove(user_input)