# Dockerfile

FROM python:3
WORKDIR /code
COPY . .

ARG port=8000
ENV PORT=${port}

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN wget https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-361.0.0-linux-x86_64.tar.gz
RUN tar -xzf google-cloud-sdk-361.0.0-linux-x86_64.tar.gz
RUN ./google-cloud-sdk/bin/gcloud init

RUN wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy
RUN chmod +x cloud_sql_proxy

CMD ["python3", "/code/src/endpoints/api.py"]
