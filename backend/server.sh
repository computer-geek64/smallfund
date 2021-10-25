#!/bin/bash
# server.sh

./google-cloud-sdk/bin/gcloud auth activate-service-account --key-file ${GCP_KEY_FILE}
./google-cloud-sdk/bin/gcloud config set project ${GCP_PROJECT_ID}

./cloud_sql_proxy -instances=${GCP_INSTANCE_CONNECTION_NAME}=tcp:3306 -credential_file ${GCP_KEY_FILE} > /dev/null 2>&1 &
sleep 3

python3 /code/src/endpoints/api.py
