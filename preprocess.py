def cleanText(text):
    #import nltk
    import re
    #import string

    #text = str(text).lower()
    #text = re.sub('\s', '', text)
    #text = re.sub('\[.*?\]', '', text)
    #text = re.sub('https?://\S+|www\.\S+', '', text)
    #text = re.sub('<.*?>+', '', text)
    #text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\t', '', text)
    text = re.sub('\n', ' ', text)
    #text = re.sub("\(cid:\d{1,2}\)", "", text)
    #text = re.sub('\W', ' ', text)
    #text = re.sub(' {2}', ' ', text)

    return(text)