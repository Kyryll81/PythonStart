FROM python:3.13.7-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "flask" "db" "upgrade && gunicorn", "--bind", "0.0.0.0:10000", "app:app" ]
