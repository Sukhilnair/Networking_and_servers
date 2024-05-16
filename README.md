# Subdomain Status Checker

## Description
This Python script checks the status of specified subdomains by sending HTTP requests and displays the status in a tabular format. It continuously checks the status every minute and updates the table accordingly.

## Requirements
- Python 3.x
- pip 3.x
- requests library (Install using `pip install requests`)

## Usage
1. Clone the repository or download the `subcheck.py` file.
2. Install the required library using `python3 -m pip install requests`.
3. Modify the `subdomains` list in the script to include the subdomains you want to monitor.
4. Run the script using the command `python3 subcheck.py`.
5. The script will continuously check the status of the subdomains and update the table every minute.

## Example
```python
import requests
import time

# List of subdomains to check
subdomains = ['mail', 'maps']

def check_status(subdomain):
    try:
        response = requests.get(f"http://{subdomain}.google.com", timeout=5)
        if response.status_code == 200:
            return "UP"
        else:
            return "DOWN"
    except requests.ConnectionError:
        return "DOWN"
    except requests.Timeout:
        return "TIMEOUT"

def print_status_table():
    print("-" * 30)
    print("| Subdomain        | Status |")
    print("-" * 30)
    for subdomain in subdomains:
        status = check_status(subdomain)
        print(f"| {subdomain.ljust(15)}.google.com | {status:6} |")
    print("-" * 30)

if __name__ == "__main__":
    print("Subdomain Status Checker")
    while True:
        print_status_table()
        time.sleep(60)  
