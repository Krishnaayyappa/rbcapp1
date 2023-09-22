import requests
import json
import os

# Directory where JSON files are stored (generated in Task 1)
json_files_directory = "/path/to/json/files"

# URL of the web service's /add endpoint
add_endpoint_url = "http://localhost:8000/add"  # Replace with your actual URL

# Iterate through JSON files in the directory
for filename in os.listdir(json_files_directory):
    if filename.endswith(".json"):
        with open(os.path.join(json_files_directory, filename), 'r') as file:
            json_data = json.load(file)

        # Send an HTTP POST request to the /add endpoint with the JSON data
        response = requests.post(add_endpoint_url, json=json_data)

        if response.status_code == 201:
            print(f"Uploaded {filename} successfully.")
        else:
            print(f"Failed to upload {filename}. Status code: {response.status_code}")
