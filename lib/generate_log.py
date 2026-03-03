# lib/generate_log.py

from datetime import datetime
import requests

def generate_log(log_data):
    """
    Writes log_data (a list of strings) to a timestamped file.
    Returns the filename.
    """

    if not isinstance(log_data, list):
        raise ValueError("Input must be a list of strings")
    
    filename = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")
    
    return filename

def fetch_data():
    """Example API request"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}

if __name__ == "__main__":
    sample_data = [
        "User logged in",
        "User updated profile",
        "Report exported"
    ]

    print("Starting script...")
    log_entries = ["User logged in", "User updated profile", "Report exported"]
    filename = generate_log(log_entries)
    print(f"Log successfully written to {filename}")
    
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
    print("Script completed successfully.")