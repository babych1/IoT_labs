FROM python:3.9-slim
WORKDIR /app
RUN pip install paho-mqtt datetime
COPY receiver.py .
CMD ["python", "receiver.py"]