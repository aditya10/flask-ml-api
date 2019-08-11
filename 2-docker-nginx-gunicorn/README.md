# Flask ML API with Docker, Gunicorn WSGI and Nginx
Building upon the first phase, we dockerize the flask app, and use Gunicorn WSGI
to achieve a much more stable and production-ready Flask API. We also use Nginx 
to interface with Gunicorn.

The model is developed in [this tutorial](https://medium.com/technonerds/using-fastais-ulmfit-to-make-a-state-of-the-art-multi-label-text-classifier-bf54e2943e83).

## Anatomy
* Gunicorn:
    * Gunicorn is a popular WSGI that works seamlessly with Flask.
    * Flask needs a Web Server Gateway Interface (WSGI) to talk to a web server.
    * Flask's built-in WSGI is not capable of handling production APIs, because it lacks security features and can only run one worker.
    * In this project, Gunicorn will start automatically in the api Docker container with the following config (see Dockerfile):
        ```
        ["gunicorn", "-w", "3", "-b", ":5000", "-t", "360", "--reload", "api.wsgi:app"]
        ```
* Nginx:
    * Nginx is a popular webserver platform. It is used to interface with gunicorn (on port 5000) and relay it to port 80.
* Docker:
    * Docker and docker-compose allow apps to be easily deployed. 
    * Using docker, we containerize our API to work independently of the environment

## How to run
* Install `docker` and `docker-compose` for your specific platform (you can easily find instructions on Google)
* Start the API using:
    ```
    docker-compose build
    docker-compose up
    ```
    This will build and spin up a virtual container with the API.
    * Building the continer for the first time will take a while, as it needs to install all requirements
    * You can use `0.0.0.0:80` to interface with it.
* You can now query `GET 0.0.0.0/classification` using [Postman](https://www.getpostman.com/) with a json body:
    ``` 
    {
    	"text": "Your classification text goes here"
    }
    ```
    It will return the associated category.