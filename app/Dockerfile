FROM python:3.9

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -r requirements.txt

COPY app.py /app

EXPOSE 5050

CMD python3 app.py
