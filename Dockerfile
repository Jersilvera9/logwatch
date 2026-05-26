# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy source code and sample logs into the container
COPY src/ ./src/
COPY sample_logs/ ./sample_logs/
COPY main.py .

# Default command - analyze the sample log file
CMD ["python", "main.py", "sample_logs/app.log"]