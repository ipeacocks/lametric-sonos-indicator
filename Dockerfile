FROM python:3-alpine

WORKDIR /app

COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "-u", "main.py"]