FROM python:3.7

WORKDIR /app

COPY main.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD echo "Hello...!"
CMD [ "python", "main.py" ]
