import pickle
import re
from model.stops import stop_words

with open('./model/model_pickle', 'rb') as f:
    imported_model = pickle.load (f)

with open('./model/vect_pickle', 'rb') as f:
    imported_vect = pickle.load (f)


def predict(text):
    text_arr = []
    text_arr.append(text)
    num_words = len(re.findall(r'\w+', text))

    res = 2
    if num_words >= 150:
        text_dtm = imported_vect.transform(text_arr)
        res = imported_model.predict(text_dtm)[0]

    return res