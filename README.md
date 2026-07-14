# 🤖 DataOps AI Assistant

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116-green)
![React](https://img.shields.io/badge/React-19-blue)
![AWS](https://img.shields.io/badge/AWS-Bedrock-orange)
![Claude](https://img.shields.io/badge/Claude-Sonnet_4-purple)

![CI](https://github.com/USUARIO/dataops-ai-assistant/actions/workflows/ci.yml/badge.svg)

---

# Descripción

DataOps AI Assistant es un asistente conversacional desarrollado con Amazon Bedrock y Claude Sonnet que permite consultar información almacenada en Amazon Athena y Amazon S3 utilizando lenguaje natural.

El proyecto implementa una arquitectura basada en herramientas (Tools), donde el modelo de lenguaje interpreta la intención del usuario y decide cuándo utilizar servicios AWS para responder consultas.

---

# Características

- Frontend desarrollado en React
- Backend desarrollado en FastAPI
- Amazon Bedrock (Claude Sonnet)
- Amazon Athena
- Amazon S3
- Tool Router
- Conversation Memory
- Respuestas en Markdown
- Swagger UI
- Arquitectura desacoplada

---

# Arquitectura

Usuario

↓

Frontend React

↓

FastAPI

↓

DataOps Agent

↓

Tool Router

↓

Athena Tool / S3 Tool

↓

AWS Bedrock

↓

Amazon Athena / Amazon S3

---

# Tecnologías utilizadas

Backend

- Python 3.12
- FastAPI
- Uvicorn
- Boto3
- Pydantic Settings

Frontend

- React
- Vite
- Axios
- React Markdown

Cloud

- Amazon Bedrock
- Claude Sonnet
- Amazon Athena
- Amazon S3
- IAM

---

# Instalación

## Clonar el proyecto

git clone ...

---

## Backend

Crear entorno virtual

python -m venv .venv

Activar entorno

Windows

.venv\Scripts\activate

Linux

source .venv/bin/activate

Instalar dependencias

pip install -r requirements.txt

Ejecutar

uvicorn main:app --reload

---

## Frontend

cd frontend

npm install

npm run dev

---

# Variables de entorno

Crear archivo .env

AWS_REGION=

BEDROCK_MODEL_ID=

BEDROCK_INFERENCE_PROFILE_ID=

ATHENA_DATABASE=

ATHENA_OUTPUT_LOCATION=

ATHENA_WORKGROUP=

S3_BUCKET=

AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

---

# API

POST

/api/v1/chat

Ejemplo

{
    "message":"¿Qué tablas tengo en Athena?"
}

---

# Ejemplos

¿Qué tablas tengo?

Muéstrame los registros de employees

¿Cuántos CSV tengo?

¿Qué archivos existen en S3?

---

# Próximas mejoras

- Agente Juez
- Sistema RAG
- Observabilidad con CloudWatch
- Dashboard
- Docker Compose
- ECS
- CI/CD

---

# Autor

Johan Mauricio Suarez Daza