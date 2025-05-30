
from mars_api_client import MarsPhotosApiClient

def test_get_and_download_photos():
    client = MarsPhotosApiClient()
    urls = client.get_photos(sol=1000, camera="fhaz")
    assert isinstance(urls, list)

    if urls:
        client.download_images(urls[:5])
