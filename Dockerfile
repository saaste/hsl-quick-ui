FROM python:3.6.8-alpine

LABEL HSL Quick UI

WORKDIR /app
EXPOSE 5000

COPY *.py ./
COPY requirements.txt .
COPY templates templates

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "server.py" ]

