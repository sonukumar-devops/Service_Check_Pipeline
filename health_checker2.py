import requests
from requests.exceptions import RequestException
import json
import sys

check_url = "http://app:5000/health" # The url we want to talk to
try:
    response = requests.get(check_url, timeout=3) # calling API using GET Request
    data = response.json()  # Turning the response text into JSON format
    
    real_response = data["status"]  #storing status response like UP or DOWN..
    print(data)
    if real_response == "UP":
        print(f"Status Returned : {real_response}")
        sys.exit(0)
    else:
        print(f"Status Returned : {real_response}")
        sys.exit(1)
except RequestException as e:
    print(f"Some other error occured: ({e})")
    sys.exit(1)
