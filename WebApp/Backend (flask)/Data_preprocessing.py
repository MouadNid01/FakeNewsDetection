import os
import pandas as pd
import json
from sklearn.utils import shuffle
import nltk
from nltk.corpus import stopwords
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

class Data_preprocessing:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.Articles_path = './Articles/{}'
        self.Real_article = ['Reuters_articles.json', 'TRTWorld_articles.json', 'TRTWorld_articles.json', \
                         'LaMap_articles.json']
        self.Fake_article = ['Breitbart_articles.json', 'NaturalNews_articles.json',\
                             'Wnd_articles.json']
        self.Vocab_size = 108192
        self.maxlen = 235
    
    def Load_articles(self, lst):
        df = pd.DataFrame(columns=['title', 'content'])
        for i in lst:
            with open(self.Articles_path.format(i), 'r') as file:
                for line in file:
                    line.strip('\n')
                    data = json.loads(line)
                    df = df.append(data, ignore_index=True)
        return df
    
    def Clean(self, text):
        """Converting the texts into lowercase characters and removing punctuations and stopwords using the nltk library."""
        text = text.lower()
        words = nltk.word_tokenize(text)
        new_words= [word for word in words if word.isalnum() and word not in self.stop_words]
        text = " ".join(new_words)
        return text
    
    def Tokenize(self, df):   
        tokenizer = Tokenizer(num_words=self.Vocab_size)
        tokenizer.fit_on_texts(df['text'])
        sequences = tokenizer.texts_to_sequences(df['text'])
        self.word_index = tokenizer.word_index
        data = pad_sequences(sequences, maxlen=self.maxlen, padding='post', truncating='post')
        return data
    
    def process(self):
        df_real = self.Load_articles(self.Real_article)
        df_fake = self.Load_articles(self.Fake_article)
        
        df_real['label'] = 1 
        df_fake['label'] = 0
        
        df_real['text'] = df_real['title']+' '+df_real['content'] 
        df_fake['text'] = df_fake['title']+' '+df_fake['content']
        
        df_real.drop(["title", "content"], axis=1, inplace= True)
        df_fake.drop(["title", "content"], axis=1, inplace= True)
        
        df = pd.concat([df_real, df_fake], axis=0, ignore_index = True)
        df = shuffle(df)
        df.drop_duplicates(inplace = True, keep='last')
        df = df.reset_index(drop= True)
        
        df['text'] = df['text'].apply(self.Clean)
        
        X = df['text'].to_frame()
        Y = df['label'].to_frame()
        padded_sequences = self.Tokenize(X)
        return (padded_sequences, Y)
        
