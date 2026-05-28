# logwatch

A Python CLI tool for parsing and analyzing server log files. Reads log file, 
categorizing each one of these entries by severity level, detecting repeated error patterns, and printing 
a summary report to the terminal.

Built this to practice working with Containerization, Kubernetes deployments, and log data.

## Usage

Run locally:
```bash
python main.py sample_logs/app.log
```

Run with Docker:
```bash
docker build -t logwatch .
docker run logwatch
```

Deploy to Kubernetes:
```bash
minikube image load logwatch:latest
kubectl apply -f k8s/job.yaml
kubectl logs job/logwatch-job
```

Run tests:
```bash
pytest tests/ -v
```
## Stack
- Python 3.11
- Docker
- Kubernetes (minikube)
- GitHub Actions (CI)
- pytest

