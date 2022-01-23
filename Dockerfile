# pull official base image
FROM python:3.10-alpine

# set work directory
WORKDIR /app


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# install psycopg2
RUN apk update \
    && apk add --virtual build-essential gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk add libffi \
    && apk add libffi-dev             

RUN apk add --update --no-cache --virtual .tmp libc-dev linux-headers zlib-dev jpeg-dev \
    && apk add libjpeg \ 
    && pip install Pillow --no-cache-dir \ 
    && apk del .tmp


# install pipenv and install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# copy project
COPY . .

# collect static files
RUN python manage.py collectstatic --noinput


# add and run as non-root user
RUN adduser -D myuser
USER myuser

# run gunicorn
CMD gunicorn orla.wsgi:application --bind 0.0.0.0:$PORT