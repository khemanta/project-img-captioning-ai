import gradio as gr
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

# Load model
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def caption_image(image):
    image = image.convert("RGB")
    inputs = processor(image, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=50)
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    return caption

demo = gr.Interface(fn=caption_image, inputs=gr.Image(), outputs="text",
                    title="Image Captioning App",
                    description="Upload an image and get a caption using BLIP model.")

demo.launch(server_name="0.0.0.0", server_port=7860)
