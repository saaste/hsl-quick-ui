FROM python:3.6.8-alpine

LABEL HSL Quick UI

WORKDIR /app
EXPOSE 5000

COPY *.py ./
COPY requirements.txt .
COPY templates templates
COPY static static

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

CMD [ "gunicorn", "-b", "0.0.0.0:5000", "server" ]

