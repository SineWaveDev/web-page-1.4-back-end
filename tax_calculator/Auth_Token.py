import requests

def generate_authentication_token():
    # Replace these values with the actual API key, secret, and version
    api_key = 'key_live_AL1pBGGBcbcWUYZfGwE8ZwUfEIz3hRl4'
    api_secret = 'secret_live_8lFpvO88BgGJwfQoQEPcGf26Enprq0Yi'
    api_version = '1.0'
    
    url = 'https://api.sandbox.co.in/authenticate'
    
    # Set the headers with API key, secret, and version
    headers = {
        'x-api-key': api_key,
        'x-api-secret': api_secret,
        'x-api-version': api_version
    }

    try:
        response = requests.post(url, headers=headers)
        response_data = response.json()
        if "access_token" in response_data:
            access_token = response_data["access_token"]
            return access_token
        else:
            print("Access token not found in the response.")
            return None

    except requests.exceptions.RequestException as e:
        print("Error occurred while making the request:", e)
        return None


if __name__ == "__main__":
    token = generate_authentication_token()
    if token:
        print("Access Token:", token)
