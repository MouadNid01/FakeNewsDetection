FROM python:slim-buster
WORKDIR /backend-flask
ADD *.txt /backend-flask
RUN pip install --upgrade pip \
    && pip install -r requirements.txt
RUN python -m nltk.downloader stopwords
RUN python -m nltk.downloader punkt
ADD . .
CMD ["python", "Flask-Backend.py"]