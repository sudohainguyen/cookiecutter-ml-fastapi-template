FROM python:3.8.2-buster

WORKDIR /app

RUN mkdir -p ./data

COPY . .

ARG BUILD_ENV=PROD
ENV MODEL_DIR=/app/data \
    ENV=$BUILD_ENV

RUN pip install --upgrade pip && pip install -r ./requirements/prod.txt

EXPOSE 80
CMD [ "uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "80"]
