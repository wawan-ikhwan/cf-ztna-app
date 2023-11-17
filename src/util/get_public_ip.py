import httpx

def get_public_ip():
  try:
    # Use a service that echoes back the public IP
    with httpx.Client() as client:
      response = client.get('http://api64.ipify.org?format=json')
        
    # Parse the JSON response
    data = response.json()
    
    # Extract and return the public IP address
    return data['ip']
  except Exception as e:
    print(f"Error: {e}")
    return None