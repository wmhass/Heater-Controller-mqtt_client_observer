# pull official base image
FROM python:3.7.4-alpine

# set work directory
WORKDIR /usr/src/mqtt_client_observer

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /usr/src/mqtt_client_observer/Pipfile
RUN pipenv install --skip-lock --system --dev

# copy project
COPY . /usr/src/mqtt_client_observer/

CMD ["python", "observer.py"]
