FROM python:3-alpine3.11

WORKDIR /app

COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "main_class.py"]