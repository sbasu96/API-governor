import yaml
import json
from pathlib import Path


def load_spec_from_content(content: bytes, filename: str) -> dict:
    if filename.endswith((".yaml", ".yml")):
        return yaml.safe_load(content)
    elif filename.endswith(".json"):
        return json.loads(content)
    else:
        raise ValueError("Unsupported file format")
