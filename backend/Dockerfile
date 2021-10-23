# Dockerfile

FROM python:3
WORKDIR /code
COPY . .

ARG port=8000
ENV PORT=${port}

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "/code/src/endpoints/api.py"]
