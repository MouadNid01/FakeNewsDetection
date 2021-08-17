import nltk
from nltk.corpus import stopwords
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


class PredHandler():
    
    def __init__(self, path):
        self.model = load_model(path)
        self.stop_words = set(stopwords.words('english'))
        self.tokenizer = Tokenizer(num_words=108192)
        
    def get_pred(self, title, text):
        self.content = self.process(title+" "+text)
        tmp = self.model.predict([self.content])[0][0]
        self.result = tmp >= 0.5
        return {"result": str(self.result), "prct": float("{:.2f}".format(tmp*100))}
            
    def process(self, text):
        text = text.lower()
        words = nltk.word_tokenize(text)
        new_words= [word for word in words if word.isalnum() and word not in self.stop_words]
        text = " ".join(new_words)
        self.tokenizer.fit_on_texts([text])
        self.sequence = self.tokenizer.texts_to_sequences([text])
        self.sequence = pad_sequences(self.sequence, maxlen=235, padding='post', truncating='post')
        return self.sequence
        
