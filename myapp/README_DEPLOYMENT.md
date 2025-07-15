# 🖼️ Image Captioning AI App with BLIP + Gradio + IBM Code Engine 🚀

This repository contains an end-to-end implementation of an **Image Captioning Web App** powered by **BLIP model** and **Gradio**, deployed using **IBM Code Engine**.

---

## ✨ Features

- 🔍 Automatically generate meaningful captions for images
- 🤖 Uses HuggingFace’s BLIP model (`Salesforce/blip-image-captioning-base`)
- 🌐 Web interface built using Gradio
- ☁️ Deployed on IBM Cloud via Code Engine (Dockerized)

---

## 📦 Project Structure

```
.
├── demo.py                  # Main Gradio app
├── Dockerfile               # Container config
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

---

## ⚙️ Setup Instructions

### 🔧 Step 1: Clone and Setup Environment

```bash
git clone https://github.com/<your-username>/project-img-captioning-ai.git
cd project-img-captioning-ai
python3 -m venv my_env
source my_env/bin/activate
pip install -r requirements.txt
```

### 🧪 Step 2: Run Locally

```bash
python3 demo.py
```

Then open your browser and go to: [http://0.0.0.0:7860](http://0.0.0.0:7860)

---

## ☁️ Deploying on IBM Code Engine

### 🔑 Prerequisites

- [x] IBM Cloud CLI
- [x] Logged in (`ibmcloud login --sso`)
- [x] Target a resource group and region

```bash
ibmcloud target -r us-east -g Default
```

### 🧱 Step-by-Step

#### 🗂️ Create and Select Project

```bash
ibmcloud ce project create --name img-captioning-ai
ibmcloud ce project select --name img-captioning-ai
```

#### 🐳 Build Docker Image

```bash
ibmcloud ce build create --name build-local-captioning   --build-type local --size large   --image us.icr.io/<your_namespace>/img-captioning-app   --registry-secret icr-secret

ibmcloud ce buildrun submit --name buildrun-local-captioning   --build build-local-captioning   --source .
```

#### 🌐 Deploy Application

```bash
ibmcloud ce application create --name img-captioning-demo   --image us.icr.io/<your_namespace>/img-captioning-app   --registry-secret icr-secret   --es 2G --port 7860 --minscale 1
```

#### 🔗 Get Public URL

```bash
ibmcloud ce app get --name img-captioning-demo --output url
```

---

## ✅ Tech Stack

- [BLIP](https://huggingface.co/Salesforce/blip-image-captioning-base)
- [Gradio](https://www.gradio.app/)
- [Transformers](https://huggingface.co/transformers/)
- [IBM Cloud Code Engine](https://www.ibm.com/cloud/code-engine)

---

## 👨‍💻 Author

**Hemant Kumar**  
[GitHub](https://github.com/khemanta)

---

🛡️ Licensed under MIT. Use with ❤️ for educational or commercial use.