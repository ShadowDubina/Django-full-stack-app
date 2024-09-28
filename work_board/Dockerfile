FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /work_board

COPY wait-for-it.sh /work_board/

COPY requirements.txt /work_board/

RUN pip install -r requirements.txt

COPY . /work_board/
