from collections import Counter

def count_by_severity(entries):
    """Count how many log entries exist for each severity level."""
    severity_counts = Counter()

    for entry in entries:
        severity_counts[entry["severity"]] += 1

    return dict(severity_counts)

def get_errors_and_criticals(entries):
    """Pull out only ERROR and CRITICAL entries for closer inspection."""
    high_priority = [
        entry for entry in entries
        if entry["severity"] in ("ERROR", "CRITICAL")
    ]
    return high_priority

def find_repeated_errors(entries, threshold=3):
    """Flag any error messages that appear more than threshold times."""
    error_messages = [
        entry["message"] for entry in entries
        if entry["severity"] in ("ERROR", "CRITICAL")
    ]

    message_counts = Counter(error_messages)

    # Only return messages that exceed the repeat threshold
    repeated = {
        msg: count
        for msg, count in message_counts.items()
        if count >= threshold
    }

    return repeated