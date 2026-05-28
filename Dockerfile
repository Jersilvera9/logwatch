# Python image
FROM python:3.11-slim

WORKDIR /app

COPY src/ ./src/
COPY sample_logs/ ./sample_logs/
COPY main.py .

# Default command - analyze the sample log file
CMD ["python", "main.py", "sample_logs/app.log"]