FROM python:3.9.5-slim-buster

WORKDIR /usr/src/app

COPY . .

RUN cd /usr/src/app && pip install -r requirements.txt

CMD ["python", "app.py"]