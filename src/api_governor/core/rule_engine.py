def check_missing_operation_ids(spec: dict):
    findings = []

    for path, methods in spec.get("paths", {}).items():
        for method, details in methods.items():
            if not isinstance(details, dict):
                continue

            if "operationId" not in details:
                findings.append({
                    "rule": "missing_operationId",
                    "path": path,
                    "method": method,
                    "message": "operationId is required"
                })

    return findings


def check_missing_descriptions(spec: dict):
    findings = []

    for path, methods in spec.get("paths", {}).items():
        for method, details in methods.items():
            if not isinstance(details, dict):
                continue

            if not details.get("description"):
                findings.append({
                    "rule": "missing_description",
                    "path": path,
                    "method": method,
                    "message": "description is required"
                })

    return findings


def run_rules(spec: dict):
    findings = []
    findings.extend(check_missing_operation_ids(spec))
    findings.extend(check_missing_descriptions(spec))
    return findings
