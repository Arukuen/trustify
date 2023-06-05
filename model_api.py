import pickle
import re
from model.stops import stop_words

# import model (MultinomialNB)
with open('./model/model_pickle', 'rb') as f: 
    imported_model = pickle.load(f)

# import vectorizer (CountVectorizer)
with open('./model/vect_pickle', 'rb') as f:
    imported_vect = pickle.load(f)

def predict(text):
    # add text to an array
    text_arr = []
    text_arr.append(text)

    # find number of words using regex
    num_words = len(re.findall(r'\w+', text))

    # res = 0 -> legitimate
    # res = 1 -> fake
    # res = 2 -> invalid

    res = 2 # default is invalid

    # if valid
    if num_words >= 150:
        # run input to the vectorizer and model
        text_dtm = imported_vect.transform(text_arr)
        res = imported_model.predict(text_dtm)[0]

    return res