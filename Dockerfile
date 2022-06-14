FROM node:buster
ENV PYTHONUNBUFFERED=1
RUN apt update
RUN yes | apt install python3
RUN apt -y install python3-pip
RUN pip3 install --no-cache --upgrade pip setuptools

RUN pip install sklearn collection webcolors opencv-python
RUN pip install scikit-image pandas numpy

WORKDIR /app
COPY ./ .
WORKDIR /app/server
RUN pip install -r requirements.txt
ENTRYPOINT ["python","server.py"]
