import json
import sys

report = "trivy-report.json"

with open(report, "r") as file:
    data = json.load(file)

critical = 0
high = 0
medium = 0
low = 0

for result in data.get("Results", []):
    vulnerabilities = result.get("Vulnerabilities", [])

    for vuln in vulnerabilities:
        severity = vuln.get("Severity", "")

        if severity == "CRITICAL":
            critical += 1
        elif severity == "HIGH":
            high += 1
        elif severity == "MEDIUM":
            medium += 1
        elif severity == "LOW":
            low += 1


print("==============================")
print(" Trivy Vulnerability Summary")
print("==============================")
print(f"CRITICAL : {critical}")
print(f"HIGH     : {high}")
print(f"MEDIUM   : {medium}")
print(f"LOW      : {low}")
print("==============================")


if critical > 0:
    print("❌ Pipeline bloqueado: existen vulnerabilidades CRITICAL")
    sys.exit(1)
else:
    print("✅ No existen vulnerabilidades CRITICAL")
    sys.exit(0)