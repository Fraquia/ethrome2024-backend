##########################################################
# Base image #############################################
##########################################################
FROM python:3.10-slim as backend

WORKDIR /app

COPY ./backend /app/backend
COPY requirements.txt /app/requirements.txt
COPY main.py /app/main.py
COPY .env /app/.env


RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]