import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
from transformers import AutoProcessor, BlipForConditionalGeneration

# Load the pretrained processor and model
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# URL of the page to scrape
url = "https://en.wikipedia.org/wiki/IBM"

# Download the page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all <img> elements
img_elements = soup.find_all('img')

# Open a file to write the captions
with open("captions.txt", "w") as caption_file:
    for img_element in img_elements:
        img_url = img_element.get('src')

        # Skip SVGs, icons, and malformed URLs
        if not img_url or 'svg' in img_url or '1x1' in img_url:
            continue
        if img_url.startswith('//'):
            img_url = 'https:' + img_url
        elif not img_url.startswith('http'):
            continue

        try:
            # Download the image
            response = requests.get(img_url, timeout=5)
            raw_image = Image.open(BytesIO(response.content)).convert('RGB')

            if raw_image.size[0] * raw_image.size[1] < 400:
                continue  # Skip tiny images

            inputs = processor(images=raw_image, text="the image of", return_tensors="pt")
            out = model.generate(**inputs, max_new_tokens=50)
            caption = processor.decode(out[0], skip_special_tokens=True)

            caption_file.write(f"{img_url}: {caption}\n")
            print(f"✅ Captioned: {img_url}")
        except Exception as e:
            print(f"❌ Error with image {img_url}: {e}")
            continue
