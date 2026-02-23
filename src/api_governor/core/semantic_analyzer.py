import re


def analyze_naming_conventions(spec: dict):
    findings = []

    for path, methods in spec.get("paths", {}).items():
        for method, details in methods.items():
            if not isinstance(details, dict):
                continue

            operation_id = details.get("operationId", "")

            # Enforce camelCase
            if operation_id and not re.match(r"^[a-z]+([A-Z][a-z0-9]+)*$", operation_id):
                findings.append({
                    "rule": "operationId_format",
                    "path": path,
                    "method": method,
                    "message": "operationId should be camelCase",
                    "suggested_fix": "Rename operationId to camelCase format"
                })

    return findings


def analyze_rest_anti_patterns(spec: dict):
    findings = []

    for path in spec.get("paths", {}).keys():
        # Avoid verbs in URL
        if any(verb in path.lower() for verb in ["create", "update", "delete", "get"]):
            findings.append({
                "rule": "rest_anti_pattern",
                "path": path,
                "method": "-",
                "message": "Avoid verbs in REST paths",
                "suggested_fix": "Use nouns in paths and HTTP methods for actions"
            })

    return findings


def analyze_versioning(spec: dict):
    findings = []

    info = spec.get("info", {})
    version = info.get("version")

    if version is None:
        findings.append({
            "rule": "missing_version",
            "message": "API version is missing in info block."
        })
        return findings

    # ✅ Normalize to string (fixes your crash)
    version_str = str(version)

    if not re.match(r"^\d+\.\d+\.\d+$", version_str):
        findings.append({
            "rule": "invalid_semver",
            "message": f"Version '{version}' is not valid semantic version (MAJOR.MINOR.PATCH)."
        })

    return findings

def run_semantic_analysis(spec: dict):
    findings = []
    findings.extend(analyze_naming_conventions(spec))
    findings.extend(analyze_rest_anti_patterns(spec))
    findings.extend(analyze_versioning(spec))
    return findings
