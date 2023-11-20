# Microservice Communication Contract

## Overview
This repository contains a Flask microservice for extracting 'page' and 'shape' IDs from JSON data. This README provides clear instructions on how to programmatically request and receive data from the microservice.

## Requesting Data

### Sending a POST Request

To request data from the microservice, you can send a POST request to the `/extract_ids` endpoint with a JSON payload containing the 'store' data. Here's an example using Python's `requests` library:

```python
import requests

# Define the JSON payload
data = {
    "store": {
        "page:page": {
            "id": 1,
            "other_data": "..."
        },
        "shape:shape_1": {
            "property": "..."
        },
        "shape:shape_2": {
            "property": "..."
        }
    }
}

# Send the POST request
response = requests.post("http://localhost:5000/extract_ids", json=data)

# Print the response
print(response.status_code)  # HTTP status code
print(response.json())       # Response data
