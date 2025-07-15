import os
import glob
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

# Load the BLIP processor and model
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Specify the local image directory
image_dir = "./local_images"
image_exts = ["jpg", "jpeg", "png"]

# Open a file to write the image captions
with open("captions.txt", "w") as caption_file:
    for ext in image_exts:
        image_paths = glob.glob(os.path.join(image_dir, f"*.{ext}"))
        for img_path in image_paths:
            try:
                raw_image = Image.open(img_path).convert('RGB')
                if raw_image.size[0] * raw_image.size[1] < 400:
                    continue  # Skip small files

                inputs = processor(images=raw_image, text="the image of", return_tensors="pt")
                out = model.generate(**inputs, max_new_tokens=50)
                caption = processor.decode(out[0], skip_special_tokens=True)

                caption_file.write(f"{img_path}: {caption}\n")
                print(f"✅ Captioned {img_path}")
            except Exception as e:
                print(f"❌ Failed to process {img_path}: {e}")
