# Roi-Olist

## Project Description

An API thats show the example of roi_value from Olist Company to be consumed in a microservices architecture,
using Django Rest Framework as the main library.

## Installation

### Creating de virtual environment:

To install the virtual environment, set this on your folder:

```bash
$ python3 -m venv venv
```
To activate your virtual environment, in macOS:

```bash
$ source venv/bin/activate
```

## Install the requirements

This command install the local dependencies that you need to running the API.

```bash
$ pip install -r requirements-dev.txt
```

## Migrate the database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

## Start the server

```bash
$ python manage.py runserver
```

ps: This API is readonly in the endpoints, create, update and delete are only available with Token authorization. 

# Documentation 

[roi-olist](https://roi-olist.herokuapp.com/)





