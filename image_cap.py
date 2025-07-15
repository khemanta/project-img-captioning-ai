from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

# Load the pretrained processor and model
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Load your image
img_path = "example_image.png"  # Make sure this matches the downloaded file
image = Image.open(img_path).convert('RGB')

# Prepare the prompt and process the image
text = "the image of"
inputs = processor(images=image, text=text, return_tensors="pt")

# Generate caption
outputs = model.generate(**inputs, max_length=50)
caption = processor.decode(outputs[0], skip_special_tokens=True)

print("🖼️ Caption:", caption)
