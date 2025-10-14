FROM python:latest
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY test_requests.py hello.py ./
EXPOSE 5000
CMD ["flask", "--app", "hello", "run", "--host=0.0.0.0", "--port=5000"]