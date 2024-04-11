FROM python:3.12

LABEL authors="Ivan"

WORKDIR /app

COPY requirements.txt .

EXPOSE 5000

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./app.py" ]
