FROM python:3.11.6

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV FLASK_ENV=docker

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]