FROM python:3.9-slim
WORKDIR /app
RUN pip install requests
COPY sensor.py .
CMD ["python", "sensor.py"]