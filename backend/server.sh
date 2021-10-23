#!/bin/bash
# server.sh

./cloud_sql_proxy -instances=${GCP_INSTANCE_CONNECTION_NAME}=tcp:3306 -credential_file ${GCP_KEY_FILE} > /dev/null 2>&1 &
python3 /code/src/endpoints/api.py
