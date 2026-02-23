from openapi_spec_validator import validate_spec
from openapi_spec_validator.validation.exceptions import OpenAPIValidationError


def validate_structure(spec: dict) -> list:
    errors = []

    try:
        validate_spec(spec)
    except OpenAPIValidationError as e:
        errors.append(str(e))
    except Exception as e:
        errors.append(str(e))

    return errors
