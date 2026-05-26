import re
from datetime import datetime

# Log severity levels we care about
SEVERITY_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

# Pattern matches standard log format: 2024-01-15 10:23:45 ERROR Some message here
LOG_PATTERN = re.compile(
    r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+"
    r"(?P<severity>[A-Z]+)\s+"
    r"(?P<message>.+)"
)

def parse_line(line):
    """Parse a single log line and return a dict, or None if it doesn't match."""
    match = LOG_PATTERN.match(line.strip())
    if not match:
        return None

    return {
        "timestamp": match.group("timestamp"),
        "severity": match.group("severity"),
        "message": match.group("message"),
    }

def parse_log_file(filepath):
    """Read a log file and return a list of parsed log entries."""
    entries = []
    skipped = 0

    with open(filepath, "r") as f:
        for line in f:
            entry = parse_line(line)
            if entry:
                entries.append(entry)
            else:
                skipped += 1

    return entries, skipped