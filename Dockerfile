FROM python:3.12

WORKDIR /home

RUN apt update && apt install -y pip
RUN pip install --upgrade pip && pip install poetry

COPY pyproject.toml /home/pyproject.toml
RUN poetry install
RUN poetry run pip install --upgrade pip 
RUN poetry run pip install openai-whisper
RUN apt install -y ffmpeg
