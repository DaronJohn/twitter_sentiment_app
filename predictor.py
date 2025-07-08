import pickle   #to load model/vectorizer
import re       #text processing
import numpy as np
import nltk     #text processing
from nltk.corpus import stopwords #used to remove words which dont have much value ex:i, an, in
from nltk.stem.porter import PorterStemmer  #used to reduce the words to their root node ex:running becomes run
nltk.download('stopwords')


#Load the saved model and vectorizer
with open('models/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('models/vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

#Preprocessing function (same logic as in training)
def preprocess_text(text):
    ps = PorterStemmer()
    text = re.sub('[^a-zA-Z]', ' ', text)   #Remove non-alphabet characters
    text = text.lower()                     #Convert to lowercase
    text = text.split()                     # okenize (split into words)
    text = [ps.stem(word) for word in text if word not in stopwords.words('english')]   #Remove stopwords + stemming
    return ' '.join(text)                   #Join back into a string

#Prediction function
def predict_sentiment(tweet, model, vectorizer):
    cleaned_tweet = preprocess_text(tweet)                      #Clean input
    vectorized_tweet = vectorizer.transform([cleaned_tweet])    #Transform into TF-IDF vector
    prediction = model.predict(vectorized_tweet)                #Get prediction
    return "Positive" if prediction[0] == 1 else "Negative"     #Return human-readable result