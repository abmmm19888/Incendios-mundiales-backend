FROM debian
RUN apt-get update
RUN apt-get install -y python3 python3-pip python3-venv
RUN python3 -m venv /venv
COPY requirements.txt .
RUN /venv/bin/pip3 install -r requirements.txt
COPY api api
WORKDIR api
CMD /venv/bin/uvicorn main:app --reload --host "$API_HOST" --port "$API_PORT"
