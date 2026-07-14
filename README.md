# 🤖 DataOps AI Assistant

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green?logo=fastapi)
![React](https://img.shields.io/badge/React-19-61DAFB?logo=react)
![AWS](https://img.shields.io/badge/AWS-Bedrock%20%7C%20Athena%20%7C%20S3-orange?logo=amazonaws)
![Claude](https://img.shields.io/badge/Claude-Sonnet%204-blueviolet)
![License](https://img.shields.io/badge/Status-Technical%20Assessment-success)

</p>

---

## 🚀 Descripción

**DataOps AI Assistant** es un asistente conversacional construido sobre una arquitectura agéntica que permite consultar información almacenada en AWS utilizando lenguaje natural.

El sistema interpreta la intención del usuario, selecciona automáticamente la herramienta adecuada y genera respuestas enriquecidas utilizando **Claude Sonnet 4** ejecutándose sobre **Amazon Bedrock**.

El asistente está diseñado para facilitar la exploración de datos empresariales almacenados en:

- Amazon Athena
- Amazon S3
- Data Catalog
- Documentación técnica

sin necesidad de escribir consultas SQL o navegar manualmente por la infraestructura AWS.

---

# 🎯 Objetivo

Reducir la complejidad del acceso a la información permitiendo que cualquier usuario consulte datos mediante preguntas en lenguaje natural.

Ejemplos:

> ¿Qué tablas existen en Athena?

> Muéstrame los primeros registros de employees

> ¿Cuántos archivos CSV tengo en el bucket?

> ¿Qué datasets existen en Bronze?

---

# 🏗 Arquitectura

Usuario
│
▼
React Frontend
│
▼
FastAPI Backend
│
▼
Claude Sonnet 4 (Amazon Bedrock)
│
├───────────────┐
│ │
▼ ▼
Athena Tool S3 Tool
│ │
▼ ▼
Amazon Athena Amazon S3


La arquitectura sigue un enfoque **Agent + Tool Calling**, donde el modelo decide cuándo utilizar una herramienta y cuándo responder directamente.

---

# ✨ Características

✅ Chat conversacional

✅ Selección automática de herramientas

✅ Consultas SQL sobre Athena

✅ Exploración de archivos en Amazon S3

✅ Memoria conversacional

✅ Prompts especializados

✅ Frontend React

✅ Backend FastAPI

✅ Arquitectura modular

✅ Preparado para RAG

---

# 🧠 Arquitectura Agéntica
DataOpsAgent

│

├── Prompt Service

├── Conversation Memory

├── Tool Selector

│

├── Athena Tool

│ └── Athena Repository

│

└── S3 Tool

└── S3 Repository


Cada componente tiene una responsabilidad única siguiendo principios SOLID.

---

# 📂 Estructura del Proyecto

app/

├── agents/

│ ├── dataops_agent.py

│ ├── tool_selector.py

│ └── tools/

│

├── api/

├── core/

├── infrastructure/

│ ├── aws/

│ │ ├── clients/

│ │ └── repositories/

│

├── memory/

├── prompts/

├── services/

└── models/

frontend/

Documents/

scripts/

logs/


---

# ⚙ Tecnologías

| Tecnología | Uso |
|------------|------|
| Python 3.12 | Backend |
| FastAPI | API REST |
| React | Frontend |
| AWS Bedrock | Inferencia LLM |
| Claude Sonnet 4 | Modelo de lenguaje |
| Amazon Athena | Consulta SQL |
| Amazon S3 | Exploración de datasets |
| Boto3 | SDK AWS |
| Vite | Frontend |


