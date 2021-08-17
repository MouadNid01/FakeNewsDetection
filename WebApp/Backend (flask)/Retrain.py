import os
from Data_preprocessing import Data_preprocessing
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import load_model
from sklearn.metrics import accuracy_score
import tensorflow as tf
import datetime

def InitializeRetraining(path):
    (sequences, Y) = Data_preprocessing().process()
    model = load_model(path) 
    
    X_train, X_test, Y_train, Y_test = train_test_split(sequences, Y, test_size=0.25,\
                                                                  random_state=25)
    Y_pred = (model.predict(X_test) >= 0.5).astype("int")
    
    accuracy = accuracy_score(list(Y_test['label']), Y_pred)
    if accuracy < 0.8:
        early_stop = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=2, restore_best_weights=True)
        model.fit(X_train, Y_train, epochs=15, validation_split=0.1, batch_size=32, shuffle=True, callbacks=[early_stop])
        Y_pred = (model.predict(X_test) >= 0.5).astype("int")
        accuracy = accuracy_score(list(Y_test['label']), Y_pred)
        with open('./model/model_info.txt', 'w') as file:
            time = datetime.now()
            file.write("Last model training in: "+time.strftime("%d-%b-%Y (%H:%M:%S)")+"\n")
            file.write("The current accuracy is: "+str(accuracy))
        model.save('./model/model1.h5')
        
    path2 = "./scraping/Articles/Reuters_articles.json"

    if os.path.exists(path2):
        os.remove(path2)
        os.remove(path2.replace("Reuters", "Nytimes"))
        os.remove(path2.replace("Reuters", "LaMap"))
        os.remove(path2.replace("Reuters", "TRTWorld"))
        os.remove(path2.replace("Reuters", "Breitbart"))
        os.remove(path2.replace("Reuters", "NaturalNews"))
        os.remove(path2.replace("Reuters", "Wnd"))
