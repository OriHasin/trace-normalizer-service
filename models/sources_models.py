from pydantic import BaseModel, Field
'''
This file contains Pydantic models for processing trace data from different monitoring systems, including DataDog, New Relic, and OpenTelemetry. 
These models are used to validate and structure trace data using aliases for mapping input fields.
you can support new data source by adding its model definition (class) to that file. 
'''


class DataDogModel(BaseModel):
    method: str = Field(..., alias="http.method")
    scheme: str = Field(..., alias="http.scheme")
    domain: str = Field(..., alias="http.domain")
    path: str = Field(..., alias="http.path")


class NewRelicModel(BaseModel):
    method: str = Field(..., alias="http.method")
    url: str = Field(..., alias="http.url")
    scheme: str = Field(..., alias="http.scheme")
    port: int = Field(..., alias="tcp.port")
    
    
class OpenTelemetryModel(BaseModel):
    domain: str = Field(..., alias="tcp.host")
    port: int = Field(..., alias="tcp.port")
    