# create venv, init venv, pip install requests

import os
import hashlib
import requests

def calculate_file_hash(file_path):
    """Calculate SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def check_hash_virustotal(api_key, file_hash):
    """Check file hash against VirusTotal API."""
    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
    headers = {
        "x-apikey": api_key
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return {"error": "Hash not found on VirusTotal."}
    else:
        return {"error": f"Unexpected error: {response.status_code}"}

def scan_directory(api_key, directory_path):
    """Scan all files in a directory against VirusTotal."""
    if not os.path.exists(directory_path):
        print("The specified directory does not exist.")
        return

    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"Processing file: {file_path}")
            file_hash = calculate_file_hash(file_path)
            print(f"Hash: {file_hash}")
            result = check_hash_virustotal(api_key, file_hash)
            if "error" in result:
                print(f"Error checking hash: {result['error']}")
            else:
                # Display a summary of the VirusTotal results
                total_engines = result['data']['attributes']['last_analysis_stats']
                print(f"VirusTotal Results for {file}: {total_engines}")

if __name__ == "__main__":
    API_KEY = "YOUR_API_KEY"  # Replace with your VirusTotal API key
    DIRECTORY_PATH = "path/to/your/directory"  # Replace with your directory path

    scan_directory(API_KEY, DIRECTORY_PATH)
