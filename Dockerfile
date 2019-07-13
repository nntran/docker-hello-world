FROM python:3.7-alpine
MAINTAINER ntran@ntdt.fr
ENV FORM_DOCKER_DIR /formation/docker
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
WORKDIR $FORM_DOCKER_DIR
COPY . $FORM_DOCKER_DIR
CMD ["flask", "run"]
