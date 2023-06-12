import pickle
import re
from model.stops import stop_words

# import model (MultinomialNB)
with open('./model/model_pickle', 'rb') as f: 
    imported_model = pickle.load(f)

# import vectorizer (CountVectorizer)
with open('./model/vect_pickle', 'rb') as f:
    imported_vect = pickle.load(f)

with open('./model/model_pickle_svm', 'rb') as f:
    imported_model_svm = pickle.load (f)
with open('./model/vect_pickle_svm', 'rb') as f:
    imported_vect_svm = pickle.load (f)

with open('./model/model_pickle_logistic_regression', 'rb') as f:
    imported_model_logistic_regression = pickle.load (f)
with open('./model/vect_pickle_logistic_regression', 'rb') as f:
    imported_vect_logistic_regression = pickle.load (f)

def predict(text):
    # add text to an array
    text_arr = []
    text_arr.append(text)

    # find number of words using regex
    num_words = len(re.findall(r'\w+', text))

    # res = 0 -> legitimate
    # res = 1 -> fake
    # res = 2 -> invalid

    res = [2, 2, 2] # default is invalid

    # if valid
    if num_words >= 150:
        # run input to the vectorizer and model
        text_dtm_nb = imported_vect.transform(text_arr)
        text_dtm_svm = imported_vect_svm.predict(text_arr)
        text_dtm_logistic_regression = imported_vect_logistic_regression.predict(text_arr)
        res = [int(imported_model.predict(text_dtm_nb)[0]),
               int(imported_model.predict(text_dtm_svm)[0]),
               int(imported_model.predict(text_dtm_logistic_regression)[0])]

    return res