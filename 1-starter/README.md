# Starter for Flask ML API
A simple flask app that returns the classification for a text entry based 
on the StackOverflow question classification model. The model is developed 
in [this tutorial](https://medium.com/technonerds/using-fastais-ulmfit-to-make-a-state-of-the-art-multi-label-text-classifier-bf54e2943e83).

## Anatomy
* `app.py` contains a script to run the flask app and create an endpoint `/classification`
* `export.pkl` is the exported fast.ai model from the tutorial.

## How to run
* Install flask and fastai packages:
    ```
    pip install flask
    pip install fastai
    ```
* Run app.py using:
    ```
    python3 app.py
    ```
    The URL of the development server will be displayed. Normally, it is `0.0.0.0:5000`.
* You can now query `GET 0.0.0.0:5000/classification` using [Postman](https://www.getpostman.com/) with a json body:
    ``` 
    {
    	"text": "Your classification text goes here"
    }
    ```
    It will return the associated category.