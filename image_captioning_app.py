import gradio as gr
import numpy as np
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

# Load the pretrained model
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Define the captioning function
def caption_image(input_image: np.ndarray):
    raw_image = Image.fromarray(input_image).convert('RGB')
    text = "the image of"
    inputs = processor(images=raw_image, text=text, return_tensors="pt")
    out = model.generate(**inputs, max_new_tokens=50)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

# Create the Gradio interface
iface = gr.Interface(
    fn=caption_image,
    inputs=gr.Image(label="Upload an image"),
    outputs="text",
    title="🖼️ Image Captioning AI App",
    description="Upload an image to receive an AI-generated caption using the BLIP model."
)

# Launch the app
iface.launch(server_name="0.0.0.0", server_port=7860)
