FROM continuumio/miniconda3:24.1.2-0

RUN apt update && apt install -y pkg-config gcc \
    default-libmysqlclient-dev pkg-config

WORKDIR /PLCSoftRel

COPY requirements.txt .
COPY .env .
COPY ./server ./server

RUN conda create -c conda-forge -p venv pymc=5.11.0 python=3.11.8 -y

SHELL ["conda", "run", "-p", "./venv", "/bin/bash", "-c"]

# install the required packages
RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["conda", "run", "--no-capture-output", "-p", "./venv", "/bin/bash", "-c", "cd server && uvicorn main:app --reload --host=0.0.0.0 --port=8000"]