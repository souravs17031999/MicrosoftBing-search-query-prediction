import joblib
import os
import re
from string import punctuation
import time
import datetime
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')
import sklearn
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


def clean_text(text):
    '''
    function to preprocess and clean the data before passing the data to model

    parameters :
        text (str) : raw unprocessed text

    returns :
        text (str) : preprocessed text ready to be passed onto the model pipeline
    '''
    STOPWORDS = set(stopwords.words('english'))
    text = text.lower()
    text = re.compile('[/(){}\[\]\|@,;]').sub(' ', text)
    text = re.compile('[^0-9a-z #+_]').sub('', text)
    text = ' '.join(word for word in text.split() if word not in STOPWORDS and word not in punctuation and len(word) > 2)
    return text

def detect_bing(input_query, model_path):
    '''
    main function for getting the predictions back to the flask app

    parameters :
        args :
        input_query (str) : url input by the user on the home page
    '''


    print(input_query)
    model = joblib.load(model_path)
    cleaned_text = clean_text(input_query)
    print(cleaned_text)
    result = model.predict([cleaned_text])
    return result
