# Fake News Detection

### Abstract
This project is an end to end web application for fake news detection, the model used in this app is based on LSTM. This model  is deployed to flask API that handles the http requests from the front-end (developed with React) and sends the classification results.

We've implemented also a retraining mechanism as a proof of concept (explained in the sections below).

This application had been dockerized in its available on docker hub you'll find installation instructions below. 

### Dataset
The dataset used in this project is the ISOT fake news dataset. this dataset contains two  csv files `True.csv` and `Fake.csv`, and it contains articles from 2016 to 2017.
* The first file named `True.csv` contains more than 12,600 articles from reuter.com.
  - True Dataset's WorldCloud


![WorldCloud1](https://github.com/MouadNid01/FakeNewsDetection/blob/main/True%20dataset's%20world%20cloud.png?raw=true)
* The second file named `Fake.csv` contains more than 12,600 articles from different fake news outlet resources.
  - Fake Dataset's WorldCloud


![WorldCloud2](https://github.com/MouadNid01/FakeNewsDetection/blob/main/fake%20dataset's%20world%20cloud.png?raw=true)


The official website of the dataset :
  - https://www.uvic.ca/engineering/ece/isot/datasets/fake-news/index.php

### Neural network architecture

![Architecture](https://github.com/MouadNid01/FakeNewsDetection/blob/main/model_schema.png?raw=true)

### Model Evaluation
* The results of this model are as follows:
  - Model Accuracy on the testing set : `0.9983`
  - Model Precision on the testing set : `0.9990`
  - Model Recall on the testing set :  `0.9973`

* **Confusion matrix**

![matrix](https://github.com/MouadNid01/FakeNewsDetection/blob/main/Confusion_matrix.png?raw=true)

* **Classification report** 

**Comming soon**
### References

**Coming soon**
