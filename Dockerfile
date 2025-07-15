# Use official lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir \
    gradio==5.23.2 \
    langchain==0.1.11 \
    transformers==4.38.2 \
    requests==2.31.0 \
    bs4==0.0.2 \
    torch==2.2.1 \
    pillow

# Set command to run app
CMD ["python", "image_captioning_app.py"]
