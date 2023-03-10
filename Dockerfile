FROM python:3.10-slim-buster

RUN apt-get update \
    && apt-get install \
       -y \
       --no-install-recommends \
       --no-install-suggests \
       git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install requests 
RUN pip install slackclient

COPY . ./app

ENV PYTHONPATH "${PYTHONPATH}:/app"

CMD ["python", "-m", "src.main"]
