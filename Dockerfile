FROM python:3-alpine3.11

WORKDIR /flask

COPY . /flask

RUN pip install -r requirements.txt

EXPOSE 3000

CMD python ./main.py