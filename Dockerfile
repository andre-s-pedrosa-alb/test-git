FROM python:3

WORKDIR /app

COPY main.py .

ENTRYPOINT python main.py
