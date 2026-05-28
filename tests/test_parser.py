import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.parser import parse_line
from src.analyzer import count_by_severity, find_repeated_errors

def test_parse_valid_line():
    line = "2024-03-01 08:17:45 ERROR Failed to connect to database"
    result = parse_line(line)
    assert result is not None
    assert result["severity"] == "ERROR"
    assert result["message"] == "Failed to connect to database"

def test_parse_invalid_line():
    line = "this is not a valid log line"
    result = parse_line(line)
    assert result is None

def test_count_by_severity():
    entries = [
        {"severity": "ERROR", "message": "something failed"},
        {"severity": "ERROR", "message": "something else failed"},
        {"severity": "INFO", "message": "all good"},
    ]
    counts = count_by_severity(entries)
    assert counts["ERROR"] == 2
    assert counts["INFO"] == 1

def test_find_repeated_errors():
    entries = [
        {"severity": "ERROR", "message": "timeout"},
        {"severity": "ERROR", "message": "timeout"},
        {"severity": "ERROR", "message": "timeout"},
        {"severity": "INFO", "message": "ok"},
    ]
    repeated = find_repeated_errors(entries, threshold=2)
    assert "timeout" in repeated
    assert repeated["timeout"] == 3
