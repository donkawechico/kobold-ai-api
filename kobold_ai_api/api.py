import os
import requests

class KoboldClient:
    def __init__(self, base_url=None):
        if base_url is None:
            base_url = os.environ.get('KOBOLD_API_BASE_URL')
        self.base_url = base_url.rstrip("/")
        self.resource_url = f"{self.base_url}/api/v1/{{command}}"

    def generate(self, payload):
        url = self.resource_url.format(command="generate")
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()["results"][0]["text"]
