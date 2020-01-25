# HSL Quick UI

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running
```bash
python3 server.py
```

## Building docker image
```bash
docker build . -t hsl-quick-ui:latest
```

## Running in docker
```bash
# Interactive
docker run --name="hsl-quick-ui" -p 5000:5000 hsl-quick-ui:latest
# As a daemon
 docker run -d --name="hsl-quick-ui" -p 5000:5000 hsl-quick-ui:latest
```
