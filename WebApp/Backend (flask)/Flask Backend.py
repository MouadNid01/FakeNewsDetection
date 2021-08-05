from flask import Flask, json, request
from apscheduler.schedulers.background import BackgroundScheduler
from PredHandler import PredHandler
#from flask_cors import CORS

Pred = PredHandler("../../Model/model1.h5")

def Retrain():
    """ Function for trigring model retrainning. """
    print("Scheduler is alive!")

sched = BackgroundScheduler(daemon=True)
sched.add_job(Retrain,'interval',minutes=1)
sched.start()

app = Flask(__name__)
#CORS(app) #comment this on deployment

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
