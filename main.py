from typing import Dict, Any
from pydantic import ValidationError
from trace_factory import TraceFactory
from models.normalization_model import NormalizedTrace



def normalize_trace(source_name: str, trace_data: Dict[str, Any]) -> NormalizedTrace:

    try:
        source_model = TraceFactory.get_source_model(source_name)
        source_instance = source_model(**trace_data)
        normalized_trace = NormalizedTrace(**source_instance.model_dump())

        return normalized_trace

    except ValidationError as e:
        print(f"Validation Error: {e}")
        raise

    except ValueError as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    # Example input data
    source_name = "datadog"
    trace_data = {
        "http.method": "GET",
        "http.scheme": "https",
        "http.domain": "example.com",
        "http.path": "/api/v1/resource",

    }

    normalized_trace = normalize_trace(source_name, trace_data)
    print(normalized_trace)