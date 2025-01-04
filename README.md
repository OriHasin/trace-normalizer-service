# Trace Normalizer Service

The **Trace Normalizer Service** is a backend solution for normalizing trace data into a standardized format. Built with extensibility and ease of maintaincence in mind, it supports configurable data formats, making it adaptable to diverse data sources and integration needs.

## Features

- **Configurable Data Formats**: Define supported APMs formats through **source models**, ensuring flexibility and adaptability - you also can modify the desired normaliztion format easily thorugh NormalizationModel! .
- **Factory Design Pattern**: The architecture enables seamless addition of new formats and processing logic.
- **Streaming Platform Integration**: Easily integrate with streaming platforms by implementing client-side logic for data ingestion and delivery.

## Getting Started

### Prerequisites

- **Python**: Ensure Python newest version is installed (Python 3.13)
- **Dependencies**: Listed in `requirements.txt`.

### Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/OriHasin/trace-normalizer-service.git
   cd trace-normalizer-service
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate 
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start running a simple test case inside main.py:
   ```bash
   python main.py
   ```
   
   

### Configuration

Supported data formats are defined in **source models**. To add a new format, add the Model to source_model.py and add the simple entry for the factory design pattern.

### Streaming Integration

To integrate the service with a streaming platform, implement a custom client to handle the ingestion of raw trace data and the retrieval of normalized outputs.



### Thank you Arad & Shani 😙 ! 
