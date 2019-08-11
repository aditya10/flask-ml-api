FROM python:3.6

#update
RUN apt-get update

#install requirements
WORKDIR /tmp
RUN pip3 install flask gunicorn
RUN pip3 install names-dataset

#copy app
COPY . /api
WORKDIR /

CMD ["gunicorn", "-w", "3", "-b", ":5000", "-t", "360", "--reload", "api.wsgi:app"]

