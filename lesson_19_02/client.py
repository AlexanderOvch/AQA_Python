import requests


BASE_URL = "http://127.0.0.1:8080"

def upload_image(file_path: str) -> str:
    with open(file_path, "rb") as img:
        response = requests.post(f"{BASE_URL}/upload", files={"image": img})
    response.raise_for_status()
    data = response.json()
    print(f"POST статус: {response.status_code} - Завантажено: {data}")
    return data["image_url"]

def get_image_info(image_url: str):
    filename = image_url.split("/")[-1]
    headers = {"Content-Type": "text"}
    response = requests.get(f"{BASE_URL}/image/{filename}", headers=headers)
    response.raise_for_status()
    print(f"GET статус: {response.status_code} - {response.json()}")
    return response.json()

def delete_image(image_url: str):
    filename = image_url.split("/")[-1]
    response = requests.delete(f"{BASE_URL}/delete/{filename}")
    response.raise_for_status()
    print(f"DEL статус: {response.status_code} - Видалено: {response.json()}")
    return response.json()

if __name__ == "__main__":
    uploaded_url = upload_image("mars_photo1.jpg")
    get_image_info(uploaded_url)
    delete_image(uploaded_url)
