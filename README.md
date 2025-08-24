# 🧾 Receipt Fraud Detection System

This project detects **fraudulent modifications in receipts** such as:
- Handwritten edits (amounts, dates, notes)
- Digital tampering (copy-paste, overlays)
- Multiple receipts in one scan
- Suspicious expense patterns

It uses **FastAPI** for the backend and integrates OCR + ML models for fraud detection.

---

## 🚀 Features
- Receipt upload endpoint
- OCR (printed + handwritten text) with Tesseract
- Fraud detection pipeline (image preprocessing + OCR → fraud model)
- Risk scoring and reporting (planned)
- API endpoints ready for integration with expense systems

---

## 📦 Tech Stack
- **Backend:** FastAPI + Uvicorn  
- **OCR:** OpenCV, Tesseract, Pillow  
- **ML/AI:** (Future) TensorFlow / Scikit-learn  
- **Database:** (Planned) PostgreSQL / Redis  
- **Deployment:** Conda / Kubernetes (optional)  

---

## ⚙️ Setup

### 1. Clone the repo
```bash
git clone https://github.com/your-username/receipt-fraud-detection.git
cd receipt-fraud-detection
```

2. Create environment
Using Conda:
```bash
conda create -n receipt-fraud python=3.9 -y
conda activate receipt-fraud
```

Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the API
```bash
python -m uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
📡 API Endpoints
GET / → Health check

POST /receipts/upload → Upload a receipt and extract text (OCR)

POST /receipts/analyze → Run fraud detection (planned)

GET /results/{id} → Retrieve analysis results (planned)

```
🛠️ Development
Folder structure:

```bash
receipt-fraud-detection/
│── src/
│   ├── main.py              # FastAPI entrypoint
│   ├── api/                 # API routes
│   ├── core/                # Core logic (OCR, fraud detection)
│   ├── ml_models/           # ML models (handwriting, tampering, receipt detection)
│   └── utils/               # Helper functions
│
│── tests/                   # Unit tests
│── docker/                  # Docker setup (optional)
│── k8s/                     # Kubernetes configs (optional)
│── README.md
│── requirements.txt
```
🔮 Roadmap

 FastAPI backend setup

 Basic OCR pipeline

 Handwriting detection model

 Digital tampering detection

 Fraud risk scoring

 API integration with expense systems

 Deployment with Kubernetes