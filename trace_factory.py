from models.sources_models import DataDogModel, NewRelicModel, OpenTelemetryModel


class TraceFactory:
    @staticmethod
    def get_source_model(source_name: str):

        source_name = source_name.lower()

        if source_name == "datadog":
            return DataDogModel

        elif source_name == "newrelic":
            return NewRelicModel

        elif source_name == "opentelemetry":
            return OpenTelemetryModel

        else:
            raise ValueError(f"Unsupported source: {source_name}")
