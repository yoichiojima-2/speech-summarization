FROM ubuntu:latest

WORKDIR /home
RUN apt update && apt install -y pip
RUN pip install --upgrade pip && pip install poetry
COPY pyproject.toml /home/pyproject.toml
COPY poetry.lock /home/poetry.lock
RUN poetry install && pip install openai-whisper
RUN apt install -y ffmpeg
