import argparse
import json
from api_governor.core.loader import load_spec
from api_governor.core.validator import validate_structure
from api_governor.core.rule_engine import run_rules
from api_governor.core.semantic_analyzer import run_semantic_analysis


def main():
    parser = argparse.ArgumentParser(description="AI API Governor")
    parser.add_argument("--file", required=True, help="Path to OpenAPI file")
    parser.add_argument("--ai", action="store_true", help="Enable AI review")
    args = parser.parse_args()

    spec = load_spec(args.file)

    structural_errors = validate_structure(spec)
    lint_errors = run_rules(spec)

    semantic_findings = run_semantic_analysis(spec)

    result = {
        "structural_errors": structural_errors,
        "lint_errors": lint_errors,
        "semantic_findings": semantic_findings
    }

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
