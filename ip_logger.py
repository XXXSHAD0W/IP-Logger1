import subprocess
import sys

def install_requests():
    try:
        import requests  # Check if requests is already installed
    except ImportError:
        print("Requests library not found. Installing it now...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
        print("Requests library installed successfully.")

def get_public_ip():
    try:
        import requests  # Import after installation check
        response = requests.get("https://api.ipify.org?format=json")
        response.raise_for_status()
        ip_address = response.json().get("ip")
        return ip_address
    except requests.RequestException as e:
        print(f"Error retrieving public IP: {e}")
        return None

# Install requests if necessary
install_requests()

# Usage
public_ip = get_public_ip()
if public_ip:
    print(f"Your public IP address is: {public_ip}")
else:
    print("Could not retrieve public IP address.")
