# 🚀 ML-via-API | Clean Architecture Machine Learning Microservice

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Railway](https://img.shields.io/badge/Railway-131415?style=for-the-badge&logo=railway&logoColor=white)](https://railway.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

An enterprise-grade, high-performance REST API built with **FastAPI** that serves two distinct, production-ready Machine Learning models. This system features fully isolated layers following **Clean Architecture** principles, robust **JWT Authentication**, and automated CI/CD deployment.

🌐 **Live Production Link:** [Deploy on Railway 🚀](https://ml-via-api-production.up.railway.app/docs#/)

---

## 🧠 Core Features & ML Pipelines

This microservice exposes advanced analytical capabilities split into two distinct domain pipelines:

### 1. SECOP II Smart Contract Recommender
* **The Problem:** Navigating hundreds of complex public procurement contracts in the SECOP II platform is highly inefficient for businesses.
* **The Solution:** An NLP-powered recommendation engine. Users submit a brief description of their company's core profile, and the model vectors the text (TF-IDF/Scikit-Learn) against a localized SECOP II CSV dataset to dynamically rank and recommend the best matching bidding opportunities.

### 2. Predictive Analytics Engine
* **The Solution:** A specialized regression/classification pipeline designed to ingest historical contract parameters and output predictive metrics (e.g., award probabilities or cost estimation values).

### 🔒 Enterprise Security & Persistence Layer
* **Robust Auth:** State-of-the-art **OAuth2 with JWT (JSON Web Tokens)** architecture. High-entropy hashing via `bcrypt` secures user data at rest.
* **Data Isolation:** Powered by **PostgreSQL** in production, orchestrated through **SQLAlchemy ORM** to ensure atomic database transactions, migrations stability, and clean repository abstractions.

---

## 🏗️ Architectural Blueprint (Clean Architecture)

The system completely decouples business logic from external frameworks, keeping the codebase incredibly scalable, testable, and maintainable.

```text
src/
├── domain/            # Pure Business Entities & Repository Interfaces (Framework agnostic)
├── use_cases/         # Application Core Rules (Orchestrates data flow and ML inferences)
└── infrastructure/    # Framework Implementations & Adapters
    ├── api/           # FastAPI Routes, Schemas (Pydantic), and Dependency Injections
    ├── database/      # SQLAlchemy Configurations, Models, and Repository Implementations
    └── security/      # JWT Generation, Password Hashing, and Middleware
