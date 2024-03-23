import requests
import json

class MLM2PROWebApi:
    def __init__(self, url: str, api_secret: str):
        self.base_url = url
        self.secret_key = "Secret"
        self.secret_value = api_secret

    def send_request(self, user_id):
        print("Sending request to Web API...")
        headers = {self.secret_key: self.secret_value}
        print(f"UserId: {user_id}, Secret Key: {self.secret_key}, Secret Value: {self.secret_value}")
        request_url = self.base_url + str(user_id)
        try:
            response = requests.get(request_url, headers=headers)
            response.raise_for_status()
            print("Web API request successful.")

            return response.text
        except Exception as ex:
            # Log or handle exceptions as needed
            # This is a basic example to return None indicating an error
            # In practice, you might want to return a custom error object or handle differently
            print(f"Error: {ex}")
            return None
