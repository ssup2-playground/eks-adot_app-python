FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY run.py run.py

CMD ["uvicorn", "run:app", "--host", "0.0.0.0", "--port", "80"]
