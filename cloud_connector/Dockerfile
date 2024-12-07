FROM python:3.9-slim
WORKDIR /app
RUN pip install flask datetime flask-cors
COPY connector.py .
CMD ["python", "connector.py"]
