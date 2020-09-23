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

## Deploy to Heroku

To deploy in Heroku you must create your own account [here](https://www.heroku.com/)

After that, to push this application, you need to install the plugin, to enable you to send informations from .env:

```bash
$ heroku plugins:install heroku-config
```
and than, push it:

```bash
$ heroku config:push -a
```
to check the configs, use this:

```bash
$ heroku config
```

To push your entire application, use the command to set your last code version to heroku:

```bash
$ git push heroku master --force (--force is optional)
```

Optional, you can enable static files, that the DRF provides, into your remote application.
To do that, you need to enable collectstatic:

```bash
$ heroku config:set DEBUG_COLLECTSTATIC=1
```

You can find more informations to enable static files in Heroku, [here](https://devcenter.heroku.com/articles/django-assets)

ps: This API is readonly in the endpoints, create, update and delete are only available with Token authorization. 

# Documentation 

[roi-olist](https://roi-olist.herokuapp.com/)





