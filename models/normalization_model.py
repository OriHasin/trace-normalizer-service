from pydantic import BaseModel, model_validator
from typing import Optional
from urllib.parse import urlparse
from route_extractor import RouteExtractor

'''
This file defines a NormalizedTrace model using Pydantic, which represents a normalized trace for HTTP or TCP-based requests. 
It is designed to handle incoming traces from various sources and transform them into a consistent format for further processing.
You can add custom properties to enrich the normalized format.
'''


class NormalizedTrace(BaseModel):
    method: Optional[str] = None
    url: Optional[str] = None
    path: Optional[str] = None
    route: Optional[str] = None
    scheme: Optional[str] = None
    domain: Optional[str] = None
    port: Optional[int] = None

    @model_validator(mode='after')
    def enrich_attributes(cls, model):

        # enrich data based on url
        if model.url:
            parsed_url = urlparse(model.url)
            print(parsed_url)
            if not model.route:  # Extract route dynamically based on URL
                model.route = RouteExtractor.extract_route(model.url)
                if not model.route:
                    model.route = parsed_url.path

            if not model.path:
                model.path = parsed_url.path

            if not model.scheme:
                model.scheme = parsed_url.scheme

            if not model.port:
                model.port = parsed_url.port or (
                    443 if parsed_url.scheme == 'https' else 80 if parsed_url.scheme == 'http' else None) or (
                    443 if model.scheme == 'https' else 80 if model.scheme == 'http' else None)

            if not model.domain:
                model.domain = parsed_url.netloc

            return model

        # enrich data, path-based
        if model.path:

            if not model.route: # Extract route dynamically based on path if there is no URL
                model.route = RouteExtractor.extract_route(model.path)
                if not model.route:
                    model.route = model.path

            if not model.port:
                model.port = 443 if model.scheme == 'https' else 80 if model.scheme == 'http' else None

        return model
