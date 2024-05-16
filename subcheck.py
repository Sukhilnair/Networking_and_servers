import requests
import time

# List of subdomains to check
subdomains = ['mail', 'maps']

def check_status(subdomain):
    try:
        url=f"http://{subdomain}.google.com"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return (url,"UP")
        else:
            return (url,"DOWN")
    except requests.ConnectionError:
        return (url,"DOWN")
    except requests.Timeout:
        return (url,"TIMEOUT")

def print_status_table():
    for subdomain in subdomains:
        url,status = check_status(subdomain)
        print(f"| {url:15}| {status:6} |")
    print("-" * 35)

if __name__ == "__main__":
    print("Subdomain Status Checker")
    print("-" * 35)
    print("| Subdomain             | Status |")
    print("-" * 35)
    while True:
        print_status_table()
        time.sleep(6) 