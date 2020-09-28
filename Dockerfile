# Base Image
FROM python:3.8.5-slim-buster

# install dependency manager
RUN pip install pipenv

# install os dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgtk-3-dev \
    tzdata \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# set default environment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# Install project dependencies
WORKDIR /app

# Install project dependencies
COPY Pipfile Pipfile.lock /app/
RUN pipenv install --system --deploy

# copy project
ADD . /app/

EXPOSE 8000

ENTRYPOINT [ "gunicorn", "--bind", "0.0.0.0:8000", "-c", "gunicorn_config.py", "--chdir", "roi_olist", "roi_olist.wsgi:application" ]