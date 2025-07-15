import requests

url = "https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    with open("./image/example_image.png", "wb") as f:
        f.write(response.content)
    print("✅ Image downloaded successfully as example_image.png")
else:
    print("❌ Failed to download image:", response.status_code)
