from flask import Flask, json, request
from apscheduler.schedulers.background import BackgroundScheduler
from PredHandler import PredHandler
from Retrain import InitializeRetraining
import os
os.chdir('./scraping')
from ScrapingHandler import InitializeScraping
os.chdir('../')

Pred = PredHandler("./model/model1.h5")

def Retrain():
    """ Function for trigring model retrainning. """
    lst = InitializeScraping()
    if __name__ == '__main__':
        for a in lst:
            a.start()
        for a in lst:
            a.join()
    
    path = "./scraping/Links_temp/Reuters_links.txt"
    if os.path.exists(path):
        os.remove(path)
        os.remove(path.replace("Reuters", "Nytimes"))
        os.remove(path.replace("Reuters", "LaMap"))
        os.remove(path.replace("Reuters", "TRTWorld"))
        os.remove(path.replace("Reuters", "Breitbart"))
        os.remove(path.replace("Reuters", "NaturalNews"))
        os.remove(path.replace("Reuters", "Wnd"))
    
    InitializeRetraining('./model/model1.h5')

sched = BackgroundScheduler(daemon=True)
sched.add_job(Retrain,'interval',minutes=60)
sched.start()

app = Flask(__name__)

@app.route("/check", methods=["POST"])
def News_check():
    """Function that takes care of prediction requests."""
    
    json_data = json.loads(request.data) # receives the JSON that contains the title and the text.
    title = json_data['title']
    text = json_data['text']
    res = Pred.get_pred(title, text) # uses the get_pred() method from the PredHandler class.
    # returns the the result as a JSON.
    return res

app.run()
