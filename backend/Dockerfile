# Dockerfile

FROM python:3.8
WORKDIR /code

RUN apt update
RUN apt install nodejs npm -y

RUN npm install crypto-js

RUN wget https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-361.0.0-linux-x86_64.tar.gz
RUN tar -xzf google-cloud-sdk-361.0.0-linux-x86_64.tar.gz

RUN wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy
RUN chmod +x cloud_sql_proxy

COPY . .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ARG port=8000
ENV PORT=${port}
ARG db_username=root
ENV DB_USERNAME=${db_username}
ARG db_password=NULL
ENV DB_PASSWORD=${db_password}
ARG gcp_key_file=hackgt8_gcp_key.json
ENV GCP_KEY_FILE=${gcp_key_file}
ARG gcp_project_id=hackgt-8-329918
ENV GCP_PROJECT_ID=${gcp_project_id}
ARG gcp_instance_connection_name=hackgt-8-329918:us-central1:hackgt8
ENV GCP_INSTANCE_CONNECTION_NAME=${gcp_instance_connection_name}

CMD ["./server.sh"]
