# Dockerfile

FROM python:3
WORKDIR /code
COPY . .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "/code/src/endpoints/api.py"]
