FROM python:3.12.0b1-buster


COPY requirements.txt /opt/
RUN pip3 install -r /opt/requirements.txt

WORKDIR /opt
#COPY . .

ENV FLASK_APP=app
ENV FLASK_DEBUG=1
CMD  ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
