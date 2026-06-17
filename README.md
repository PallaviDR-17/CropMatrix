![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Machine Learning](https://img.shields.io/badge/AI-Scikit--Learn-orange)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Production--Ready-brightgreen)

# 🌾 CropMatrix

### AI-Powered Smart Agriculture & Crop Recommendation Platform

CropMatrix is a full-stack intelligent agriculture platform that combines **FastAPI, PostgreSQL, Machine Learning, and Streamlit** to help farmers make data-driven decisions. The system analyzes environmental parameters such as temperature, humidity, and soil moisture to provide smart crop recommendations through an interactive dashboard.

---

## 🚀 Features

* 🔐 **JWT Authentication** – Secure user registration and login
* 🌱 **Sensor Data Management** – Store and monitor temperature, humidity, and soil moisture data
* 🤖 **AI Crop Recommendation Engine** – Predicts the most suitable crop based on field conditions
* 📊 **Interactive Streamlit Dashboard** – User-friendly interface for farmers and administrators
* 🗄️ **Database Integration** – Persistent storage using PostgreSQL or SQLite
* 🐳 **Docker Support** – Easy deployment and scalability

---

## 🛠️ Technology Stack

### Backend

* FastAPI
* Python 3.11
* SQLAlchemy

### Database

* PostgreSQL / SQLite

### Machine Learning

* Scikit-learn
* Pandas
* NumPy

### Frontend

* Streamlit

### Security

* JWT Authentication
* Passlib (bcrypt)

### Deployment

* Docker
* Docker Compose

---

## 📂 Project Structure

```text
cropmatrix/
│
├── backend/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   └── routes/
│       ├── auth_routes.py
│       ├── sensor_routes.py
│       └── ai_routes.py
│
├── ai_models/
│   ├── dataset.csv
│   ├── train_model.py
│   └── crop_model.pkl
│
├── dashboard/
│   └── app.py
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
└── .gitignore
```

---

## ⚙️ Installation & Setup
📥 Clone the Repository

Clone the project to your local machine:

git clone https://github.com/PallaviDR-17/CropMatrix.git
cd CropMatrix

### Create Virtual Environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄️ Database Configuration

### PostgreSQL

```sql
CREATE DATABASE cropmatrix;
CREATE USER your_username WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE cropmatrix TO your_username;
```

Update database credentials in:

```text
backend/config.py
```

---

## ▶️ Run Backend

```bash
python -m uvicorn backend.main:app --reload
uvicorn backend.main:app --reload
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## ▶️ Run Dashboard

```bash
python -m streamlit run dashboard/app.py
```

---

## 🐳 Docker Deployment

```bash
docker-compose up --build
```

---

## 📖 Usage

### 1. Register/Login

Create a new account and securely log in using JWT authentication.

### 2. Enter Sensor Data

Provide:

* Temperature
* Humidity
* Soil Moisture

### 3. Get AI Recommendation

CropMatrix analyzes environmental conditions and recommends the most suitable crop.

---

## 🌟 Key Highlights

* Secure Authentication System
* Real-Time Sensor Monitoring
* AI-Powered Crop Prediction
* FastAPI REST APIs
* Interactive Dashboard
* Production-Ready Architecture

---

## 👨‍💻 Developed By

**Pallavi D R**

### CropMatrix

**"Turning Farm Data into Smart Decisions."**
