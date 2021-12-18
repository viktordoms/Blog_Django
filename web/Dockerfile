FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /blog_django

WORKDIR /blog_django

COPY ./requirements.txt /blog_django

RUN  pip install --upgrade pip && pip install -r requirements.txt

CMD ./wait-for-it.sh  db:3306 --  python3 ./blog_django/manage.py runserver 0.0.0.0:8000
