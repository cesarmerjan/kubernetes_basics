FROM python:3.9.0-slim-buster

WORKDIR /authentication

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN pip install gunicorn

COPY src src

ENV FLASK_APP=src.app:app

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "1",  "--threads", "8",  "src.app:app"]