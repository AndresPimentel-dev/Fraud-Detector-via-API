# 🚀 ML-via-API | Fraud Detection Microservice

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Railway](https://img.shields.io/badge/Railway-000000?style=for-the-badge&logo=railway&logoColor=white)](https://railway.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

An enterprise-grade, high-performance REST API built with **FastAPI** designed for **Real-time Fraud Detection**. This system features fully isolated layers following **Clean Architecture** principles, robust **JWT Authentication**, and is fully containerized.

---

## 🌐 Live Demo & Documentation

Puedes acceder a la documentación interactiva (Swagger UI) del servicio desplegado en producción aquí:

👉 **[Documentación API - Railway](https://fraud-detector-via-api-production.up.railway.app/docs)**

---

## 🧠 ML Model: Fraud Detection Engine

* **The Problem:** Identifying fraudulent transactions in real-time to mitigate financial risk and prevent unauthorized activities.
* **The Solution:** A specialized classification pipeline designed to ingest transactional data and output a fraud probability score, enabling automated risk assessment and decision-making.

---

## 🚀 Quick Start (Docker Compose)

Este proyecto está configurado para ejecutarse rápidamente mediante **Docker Compose**. Esto levantará tanto la API como la base de datos necesaria de forma aislada.

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/AndresPimentel-dev/ML-via-API](https://github.com/AndresPimentel-dev/ML-via-API)
   cd ML-via-API