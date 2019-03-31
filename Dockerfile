FROM python:3.5
RUN apt-get update
RUN mkdir /app
COPY . /app/
WORKDIR /app
RUN pip install -r requirements.txt
RUN python manage.py migrate

