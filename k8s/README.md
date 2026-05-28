# logwatch

A Python CLI tool that parses log files, detects error patterns, and flags anomalies by severity. Containerized with Docker and deployable to Kubernetes.


- Parses structured log files and categorizes entries by severity (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Detects repeated error messages that exceed a frequency threshold
- Outputs a clean summary report to the terminal

## Run locally

```bash
python main.py sample_logs/app.log
```

## Run with Docker

```bash
docker build -t logwatch .
docker run logwatch
```

## Deploy to Kubernetes

```bash
minikube image load logwatch:latest
kubectl apply -f k8s/job.yaml
kubectl logs job/logwatch-job
```

## Project structure

```
logwatch/
├── src/
│   ├── parser.py      # Log file reader and regex parser
│   └── analyzer.py    # Severity counter and anomaly detection
├── sample_logs/
│   └── app.log        # Sample log file for testing
├── k8s/
│   └── job.yaml       # Kubernetes Job manifest
├── main.py            # CLI entry point
└── Dockerfile
```