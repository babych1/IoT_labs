FROM python:3.9-slim
WORKDIR /app
RUN pip install Flask requests
COPY gateway.py .
CMD ["python", "gateway.py"]