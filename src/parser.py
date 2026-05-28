import re
from datetime import datetime

SEVERITY_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


LOG_PATTERN = re.compile(
    r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+"
    r"(?P<severity>[A-Z]+)\s+"
    r"(?P<message>.+)"
)

def parse_line(line):
    """Parse single log line, return a dict, or None if they do not match."""
    match = LOG_PATTERN.match(line.strip())
    if not match:
        return None

    return {
        "timestamp": match.group("timestamp"),
        "severity": match.group("severity"),
        "message": match.group("message"),
    }

def parse_log_file(filepath):
    """Read log file and return list of parsed log entries."""
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