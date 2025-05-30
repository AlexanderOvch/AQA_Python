from http.client import responses
import requests
import os
from dotenv import load_dotenv
from requests import Response

load_dotenv()

class BaseApiClient:

    BASE_URL = os.getenv("NASA_API_URL")

    def __init__(self):
        self._session = requests.Session()
        self._session.params = {
            "api_key": os.getenv("NASA_API_KEY")
        }

    def _get(self, params: dict = None) -> Response:
        combined_params = self._session.params.copy()
        if params:
            combined_params.update(params)
        return self._session.get(url=self.BASE_URL, params=combined_params)

class MarsPhotosApiClient(BaseApiClient):
    def get_photos(self, sol, camera: str) -> list[str]:
        params = {
            "sol": sol,
            "camera": camera
        }
        response = self._get(params=params)
        response.raise_for_status()
        data = response.json()
        return [photo["img_src"] for photo in data["photos"]]

    def download_images(self, image_urls: list[str]):
        for idx, url in enumerate(image_urls[:5], 1):
            response = self._session.get(url)
            response.raise_for_status()
            with open(f"mars_photo{idx}.jpg", "wb") as f:
                f.write(response.content)

if __name__ == "__main__":
    client = MarsPhotosApiClient()
    urls = client.get_photos(sol=1000, camera="fhaz")
    print(f"Found {len(urls)} photos.")
    client.download_images(urls)
    print("Downloaded photos.")