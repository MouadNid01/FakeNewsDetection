from ScrapingHandler import InitializeScraping
from flask import Flask, json, request
from apscheduler.schedulers.background import BackgroundScheduler
from PredHandler import PredHandler
from Retrain import InitializeRetraining
import atexit

Pred = PredHandler("./model/model1.h5")

def Retrain():
    """ Function for trigring model retrainning. """
    lst = InitializeScraping()
    print('#########################')
    if __name__ == '__main__':
        for a in lst:
            a.start()
        for a in lst:
            a.join()
    
    InitializeRetraining('./model/model1.h5')


sched = BackgroundScheduler(daemon=True)
sched.add_job(Retrain,'interval',hours=2)
sched.start()
# Shut down the scheduler when exiting the app
atexit.register(lambda: sched.shutdown())


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

@app.route("/")
def test():
    msg = '<center> <h3> The api is working <br />'
    with open('./model/model_info.txt', 'r') as file:
        for line in file:
            msg += line +'<br />'
    msg += '</h3> </center>'
    return msg

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


