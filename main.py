import sys
from src.parser import parse_log_file
from src.analyzer import count_by_severity, get_errors_and_criticals, find_repeated_errors

def print_report(filepath, entries, skipped):
    severity_counts = count_by_severity(entries)
    high_priority = get_errors_and_criticals(entries)
    repeated = find_repeated_errors(entries, threshold=2)

    print(f"\n{'='*50}")
    print(f"  logwatch report: {filepath}")
    print(f"{'='*50}")
    print(f"  Total entries parsed : {len(entries)}")
    print(f"  Lines skipped        : {skipped}")
    print()

    print("  Breakdown by severity:")
    for level in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        count = severity_counts.get(level, 0)
        print(f"    {level:<10} {count}")

    if repeated:
        print()
        print("  Repeated errors (2+ occurrences):")
        for msg, count in repeated.items():
            print(f"    [{count}x] {msg}")

    if high_priority:
        print()
        print("  ERROR / CRITICAL entries:")
        for entry in high_priority:
            print(f"    {entry['timestamp']}  {entry['severity']:<8}  {entry['message']}")

    print(f"{'='*50}\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <path-to-logfile>")
        sys.exit(1)

    filepath = sys.argv[1]
    entries, skipped = parse_log_file(filepath)
    print_report(filepath, entries, skipped)