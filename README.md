# Fake News Detection Using Deep Learning

### Abstract
This project is an end to end web application for fake news detection. The model was built using Long short-term memory (LSTM) which is an artificial recurrent neural network (RNN) architecture used in the field of deep learning. Our model was deployed to flask API that handles the HTTP requests from the front-end (developed with React) and sends the classification results to the user.

We've implemented also a ```retraining mechanism``` as a proof of concept (explained in the sections below).

Both the front-end and the API had been dockerized and they are available on docker hub; you'll find installation instructions below. 

### Dataset
The dataset used to train the model is the ISOT fake news dataset, it contains two  csv files :  `True.csv` and `Fake.csv`. 

* The first file named `True.csv` contains more than 12,600 articles from reuter.com.
  - ```True Dataset's WorldCloud```

<p align="center"><img src="https://github.com/MouadNid01/FakeNewsDetection/blob/main/Images/True%20dataset's%20world%20cloud.png?raw=true" /></p>

* The second file named `Fake.csv` contains more than 12,600 articles from different fake news outlet resources.
  - ```Fake Dataset's WorldCloud```

<p align="center"><img src="https://github.com/MouadNid01/FakeNewsDetection/blob/main/Images/Fake%20dataset's%20world%20cloud.png" /></p>


The official website of the dataset :
  - https://www.uvic.ca/engineering/ece/isot/datasets/fake-news/index.php

### Neural network architecture

<p align="center"><img src="https://github.com/MouadNid01/FakeNewsDetection/blob/main/Images/model_schema.png?raw=true" /></p>

### Model Evaluation
* The results of this model are as follow:
  - Model Accuracy on the testing set : `0.9989`
  - Model Precision on the testing set : `0.9996`
  - Model Recall on the testing set :  `0.9981`

* **Confusion matrix**
<p align="center"><img src="https://github.com/MouadNid01/FakeNewsDetection/blob/main/Images/Confusion_matrix.png?raw=true" /></p>

### Retraining
In order to keep the model updated we've implemented a retraining mechanism that consits of 2 steps:
* **Step 1:** Web scraping of the news websites
  - The websites used for getting the reliable news are: *Reuters, Nytimes, LaMap, TrtNews*
  - The websites used for getting the fake news are: *Breitbart, NaturalNews, Wnd.* (you can find the code for scraping the InfoWars website) as comments in FakeLinks_scraping.py. 
* **Step 2:** After cleaning the scrapped data we test the model accuracy on it, if the accuracy is below 80% we retrain the model using the new data.

This process is summarized in the figure below:
<p align="center"><img  src="https://raw.githubusercontent.com/MouadNid01/FakeNewsDetection/main/Images/Model%20retraining.jpg" /></p>

### Intallation instructions
This web app is available on docker hub via [link](https://hub.docker.com/repository/docker/mouadnid00/fake-news-detection/general).
The api is available under the docker tag `api`. and the frontend under the tag `front`.

To install this app use the file `docker-compose.yml` you'll find it under the ```webapp``` folder.

 To pull the images(front-end & API) run: 

 ```
 $ docker-compose pull 
 ``` 
 

 To run the containers: 
```
$ docker-compose up
``` 
### Api example

<p align="center"><img  src="https://raw.githubusercontent.com/MouadNid01/FakeNewsDetection/main/Images/Request%20example.png" /></p>

### References

**Coming soon**
