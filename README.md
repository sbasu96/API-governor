# 📘 API Governor

A lightweight, AI-assisted API governance and linting tool designed to enforce consistency, best practices, and compliance across API specifications.

API Governor analyzes OpenAPI/Swagger definitions and flags structural, semantic, and design inconsistencies before they reach production.

---

## 🚀 Why API Governor?

In distributed systems, inconsistent APIs create:

- Versioning conflicts  
- Schema drift  
- Naming inconsistencies  
- Documentation gaps  
- Governance overhead  

API Governor helps teams shift API validation **left in the development lifecycle**, reducing downstream rework.

---

## ✨ Features

- 🔍 OpenAPI (v2/v3) specification validation  
- 🧠 AI-based rule evaluation  
- 📊 Structured linting reports  
- ⚙️ Extensible rule engine  
- 🖥️ Web UI with real-time feedback  
- 📁 Static file support (FastAPI backend)

---

## 🏗️ Tech Stack

- Backend: FastAPI  
- ASGI Server: Uvicorn  
- Language: Python  
- Frontend: HTML + CSS  
- Spec Standard: OpenAPI Specification  

---

## 📂 Project Structure

src/
├── api_governor/
│   ├── core/
|   |    └── loader.py
│   |    └── models.py
|   |    └── rule_engine.py
|   |    └── semantic_analyzer.py
|   |    └── validator.py
|   |
│   ├── web
|   |    ├── static
|   |    |     └── styles.css
|   |    ├── templates/
│   |    |    └── index.html
│   |    |    └── base.html
|   |    |    └── results.html
|   |    ├── app.py
|   |    ├── routes.py
|   |    
|   ├── main.py
├── requirements.txt
├── README.md
└── .gitignore
