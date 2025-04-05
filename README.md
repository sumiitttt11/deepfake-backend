# 🧠 Deepfake Detection App

This project is a full-stack application that detects deepfakes in images using a deep learning model (EfficientNet). The **frontend** is built with **React**, and the **backend** is powered by **FastAPI** with a trained model.

---

## 📂 Project Structure

```text
deepfake/
├── backend/           # FastAPI backend
│   ├── app/
│   │   ├── model/     # Model loading & prediction logic
│   │   ├── utils/     # Image preprocessing utilities
│   │   └── ...
│   ├── main.py        # FastAPI entry point
│   └── requirements.txt
│
└── frontend/          # React frontend
    ├── src/
    └── package.json
```

## 🔧 How to Run

**1. Clone the repository**
```
git clone https://github.com/sumiitttt11/Image_Deepfake-detection
```
**2. Navigate to project directory**
```
cd deepfake
```
**⚛️Frontend Setup**
**For Frontend**
```bash
https://github.com/sumiitttt11/deepfake-frontend
```
**🐍 Backend Setup:**
```bash
cd backend
pip install -r requirements.txt    # Install dependencies
uvicorn main:app --reload          # Run the backend
```
#### The backend will run at http://localhost:8000 and frontend at http://localhost:3000.

## 🧪 How It Works
- Upload an image or video using the web interface.
- The file is sent to the FastAPI backend.
- The model processes and detects if it’s real or a deepfake.
- Results are displayed.

---

## ❓ For any Queries

Feel free to reach out:

<p align="left">
  <a href="https://instagram.com/sumiiitt.af" target="_blank">
    <img src="https://img.icons8.com/fluency/48/instagram-new.png" alt="Instagram" />
  </a>
  <a href="https://linkedin.com/in/sumiitttt11/" target="_blank">
    <img src="https://img.icons8.com/fluency/48/linkedin.png" alt="LinkedIn" />
  </a>
  <a href="mailto:kumawatsumit984@gmail.com" target="_blank">
    <img src="https://img.icons8.com/fluency/48/gmail-new.png" alt="Gmail" />
  </a>
</p>

---
