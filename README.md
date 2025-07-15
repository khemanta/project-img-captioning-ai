
# 🖼️ AI Image Captioning App with BLIP and Gradio

This project demonstrates how to build a powerful and user-friendly image captioning application using the **BLIP model** from Hugging Face and a **Gradio** interface. The app can caption images from files, URLs, or folders and supports a business scenario for news media automation.

---

## ✨ Features

- 🧠 **Image captioning** using the BLIP model from Hugging Face.
- 🌐 **Web interface** using Gradio for interactive use.
- 🌍 **Web scraping** to auto-caption images from any webpage.
- 🗂️ **Batch processing** for local image folders.
- 💼 **Business Use Case**: Newsroom automation for accessibility & SEO.

---

## 📦 Requirements

Install the following in a virtual environment:

```bash
pip install langchain==0.1.11 gradio==5.23.2 transformers==4.38.2 bs4==0.0.2 requests==2.31.0 torch==2.2.1
```

---

## 🛠️ Files in the Project

| File                      | Purpose                                             |
|---------------------------|-----------------------------------------------------|
| `image_cap.py`            | Caption one image from local file                  |
| `image_captioning_app.py` | Gradio web app interface                            |
| `automate_url_captioner.py`| Extract & caption all images from a webpage       |
| `caption_local_folder.py` | Caption all images from a local folder              |
| `hello.py`                | Sample hello Gradio app                             |
| `download_image.py`       | Python script to download image via requests        |
| `captions.txt`            | Output file with image URLs and their captions      |

---

## 🚀 Quick Start

### 🔹 1. Virtual Environment Setup

```bash
pip install virtualenv
virtualenv my_env
source my_env/bin/activate
```

### 🔹 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔹 3. Run Local Script

```bash
python image_cap.py
```

### 🔹 4. Run Gradio App

```bash
python image_captioning_app.py
```

### 🔹 5. Auto-caption Images from Web

```bash
python automate_url_captioner.py
```

### 🔹 6. Caption All Images in Local Folder

```bash
python caption_local_folder.py
```

---

## 🧪 Sample Output

A sample caption generated:
> 🖼️ "a beautiful view of the ocean with waves and cloudy sky"

---

## 🌐 Deployment

To deploy this app on a cloud service or Hugging Face Spaces:
- Package the app with a `requirements.txt`
- Expose port 7860
- Set `host='0.0.0.0'` in Gradio `launch()`

---

## 📁 .gitignore

```
.theia/
*.log
captions.txt
```

---

## 🔗 GitHub

Repo URL: [https://github.com/khemanta/project-img-captioning-ai](https://github.com/khemanta/project-img-captioning-ai)

---

## 🧠 Author

**Hemant, K.**  
✉️ kumar.hemant.iitg@gmail.com  
🔗 [GitHub/khemanta](https://github.com/khemanta)

---

## 📄 License

MIT License
