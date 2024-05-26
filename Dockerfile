FROM python:3.12-slim

COPY ./requirements.txt /app/

WORKDIR /app/

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY ./.env /app/

COPY ./backend /app/backend