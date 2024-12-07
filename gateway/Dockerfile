FROM python:3.9-slim
WORKDIR /app
RUN pip install paho-mqtt
COPY gateway.py .
CMD ["python", "gateway.py"]
