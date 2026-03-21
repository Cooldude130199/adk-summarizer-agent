# 🚀 Gemini Summarizer Service  
### *AI-Powered Text Summarization on Google Cloud Run*

---

## 📖 Overview  
The **Gemini Summarizer Service** is a production-ready AI agent built with **Google’s Agent Development Kit (ADK)** and powered by the **Gemini model**.  
It provides **text summarization as a service**, deployed on **Google Cloud Run** for scalability, security, and ease of integration.  

Users send raw text via an HTTP POST request, and the agent returns a concise, actionable summary in JSON format.  

---

## ✨ Key Features  
- 🤖 **AI Summarization** using Gemini  
- ☁️ **Serverless Deployment** on Cloud Run  
- 🔗 **RESTful API Endpoint** for easy integration  
- 🔒 **Secure IAM Authentication**  
- 💡 **Lightweight & Cost-Efficient**  

---

## 🛠️ Tech Stack  
- **Google ADK** – Agent framework  
- **Gemini Model** – Generative AI inference  
- **Python + Flask** – Service layer  
- **Docker** – Containerization  
- **Cloud Run** – Serverless hosting  

---

## 🔄 Process Flow  
```mermaid
flowchart LR
    A[User] --> B[Cloud Run Service]
    B --> C[ADK Agent]
    C --> D[Gemini Model]
    D --> E[Response to User]
