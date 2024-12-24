FROM python:3.9-slim
RUN pip install paho-mqtt
WORKDIR /app
COPY sensor.py /app/
CMD ["python", "sensor.py"]
