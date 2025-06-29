import json
import sys

def check_quality_gate(report_file):
    with open(report_file, 'r') as f:
        data = json.load(f)

    violations = data.get("results", {}).get("violations", [])
    
    # Filter for HIGH or CRITICAL severity violations
    high_critical_violations = [
        v for v in violations if v.get("severity") in ("HIGH", "CRITICAL")
    ]

    count = len(high_critical_violations)
    
    if count > 0:
        print(f"Quality Gate FAILED: Found {count} HIGH or CRITICAL severity violations.")
        sys.exit(1)
    else:
        print("Quality Gate PASSED: No HIGH or CRITICAL severity violations found.")
        sys.exit(0)

if __name__ == "__main__":
    report_file = "report.json"  # change if your file has a different name/path
    check_quality_gate(report_file)