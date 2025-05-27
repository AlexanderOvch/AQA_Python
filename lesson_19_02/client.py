import requests

with open("mars_photo1.jpg", "rb") as img:
    r_post = requests.post("http://127.0.0.1:8080/upload", files={"image": img})
data = r_post.json()
print(f"POST статус: {r_post.status_code} - Завантажено: {data}")

filename = data["image_url"].split("/")[-1]

headers = {"Content-Type": "text"}
r_get = requests.get(f"http://127.0.0.1:8080/image/{filename}", headers=headers)
print(f"GET статус: {r_get.status_code} - {r_get.json()}")

r_del = requests.delete(f"http://127.0.0.1:8080/delete/{filename}")
print(f"DEL статус: {r_del.status_code} - Видалено:", r_del.json())
