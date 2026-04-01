# FastAPI CI/CD Demo (Python 3.12 + GitHub Actions + Render Deployment)

This is a simple demonstration of CI/CD by deploying a Python **FastAPI** application using:

- **GitHub Actions** for CI/CD  
- **Python 3.12**  
- **Pytest** for automated testing 
- **Render.com** for hosting  

---

## 🚀 Live Demo

Once deployed, your API will be available at: ```https://<your-render-service-name>.onrender.com/```

Example endpoints:

- `/` → returns a greeting  
- `/sum/{a}/{b}` → returns the sum of two numbers  

---

## 📂 Project Structure

```
.
├── app/
│   ├── main.py
├── requirements.txt
└── .github/
    └── workflows/
        └── deploy.yaml
```

### Running Locally
#### 1. Create and Activate virtual environment
```
python3 -m venv venv

source venv/bin/activate  # macOS / Linux
venv\Scripts\activate     # Windows
```

#### 2. Install dependencies

```pip install -r requirements.txt```

#### 2. Start Fast API Locally

```uvicorn app.main:app --reload```

#### 3. Run Test Locally
```pytest```

#### 4. Open in your browser
```http://127.0.0.1:8000```

### 🛠 GitHub Actions CI/CD Pipeline

#### 1. Set Render Secret
Set the secret `RENDER_DEPLOY_HOOK` in GitHub → Settings → Secrets → Actions → New secret with the value you get from render.com

The workflow location can be found here: 
```.github/workflows/deploy.yml```

