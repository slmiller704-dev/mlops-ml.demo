# Intelligent Agricultural Supply Chain Complaint Resolution System

This project is a scalable, end-to-end AI-assisted solution designed to transform agricultural supply chain complaint management from a reactive process into a proactive, intelligent resolution pipeline.

Project Overview
The platform utilizes a combination of machine learning, semantic retrieval (RAG), and agentic multi-agent orchestration to automatically classify, analyze, investigate, and draft resolution workflows for customer complaints.

---

System Architecture & Workflow

1. Data Preparation & Exploration (`Task 1`)
* **Data Ingestion**: Loads or generates synthetic datasets simulating agricultural supply chain issues (e.g., *Delayed Delivery*, *Damaged Fertilizer*, *Spoiled Seeds*).
* **Preprocessing**: Normalizes raw customer text, filters stop words, and applies custom label encoders.
* **Class Balancing**: Utilizes class resampling to balance heavily skewed categories ensuring robust learning.

2. Machine Learning & Knowledge Base (`Task 2`)
   Sentence Embeddings: Converts clean complaint text into dense vector representations using `SentenceTransformer` (`all-MiniLM-L6-v2`).
* **ANN Classifier**: A PyTorch-based Artificial Neural Network (ANN) that automatically categorizes incoming complaints into one of the 8 target domains.
* **RAG Retrieval**: Leverages a dense `FAISS` vector index mapping complaints to historical Standard Operating Procedures (SOPs) for context-aware policy retrieval.

3. Agentic AI Orchestration (`Task 3`)
Built on top of **LangGraph**, the system coordinates a graph of specialized collaborative LLM nodes:
* **Analyzer Agent**: Assesses severity and flags critical high-risk accounts (e.g., contamination, legal escalation).
* **Investigator Agent**: Automatically queries the FAISS-powered SOP database.
* **Planner Agent**: Generates actionable, step-by-step resolution blueprints.
* **Communicator Agent**: Drafts empathetic, customized email replies to affected customers.
* **Escalation Manager**: Ensures high-risk edge cases are properly isolated and directly formatted into structured executive reports.

4. Interactive Dashboards & Deployment (`Task 4`)
* **FastAPI Backend**: Exposes the orchestration graph as high-performance endpoints.
* **Unified Streamlit Interface**: Offers four functional views from a single viewport:
  1. **EDA Dashboard** for overall operation health metrics.
  2. **Real-time ANN Classifier** playground.
  3. **RAG Search Assistant** for policy lookups.
  4. **Agentic Workflow Trace** to inspect LangGraph execution logs.
* **Docker Containerization**: Includes modular configuration via `docker-compose.yml` to orchestrate service microstructures on independent virtual ports.

---

How to Run

Local Installation
Ensure you have the required dependencies from `requirements.txt` installed:
```bash
pip install -r requirements.txt
Run via Docker Compose
Build and boot up the microservice network with a single command:

docker-compose up --build
FastAPI Backend: http://localhost:8000
Unified Streamlit Platform: http://localhost:8501

# Intelligent Agricultural Supply Chain Complaint Resolution System

This project is a scalable, end-to-end AI-assisted solution designed to transform agricultural supply chain complaint management from a reactive process into a proactive, intelligent resolution pipeline.

Project Overview
The platform utilizes a combination of machine learning, semantic retrieval (RAG), and agentic multi-agent orchestration to automatically classify, analyze, investigate, and draft resolution workflows for customer complaints.

---

System Architecture & Workflow

1. Data Preparation & Exploration (`Task 1`)
  Data Ingestion: Loads or generates synthetic datasets simulating agricultural supply chain issues (e.g., *Delayed Delivery*, *Damaged Fertilizer*, *Spoiled Seeds*).
  Preprocessing: Normalizes raw customer text, filters stop words, and applies custom label encoders.
  Class Balancing: Utilizes class resampling to balance heavily skewed categories ensuring robust learning.

2. Machine Learning & Knowledge Base (`Task 2`)
  Sentence Embeddings: Converts clean complaint text into dense vector representations using `SentenceTransformer` (`all-MiniLM-L6-v2`).
  ANN Classifier: A PyTorch-based Artificial Neural Network (ANN) that automatically categorizes incoming complaints into one of the 8 target domains.
  RAG Retrieval: Leverages a dense `FAISS` vector index mapping complaints to historical Standard Operating Procedures (SOPs) for context-aware policy retrieval.

3. Agentic AI Orchestration (`Task 3`)
Built on top of LangGraph, the system coordinates a graph of specialized collaborative LLM nodes:
  Analyzer Agent: Assesses severity and flags critical high-risk accounts (e.g., contamination, legal escalation).
  Investigator Agent: Automatically queries the FAISS-powered SOP database.
  Planner Agent: Generates actionable, step-by-step resolution blueprints.
  Communicator Agent: Drafts empathetic, customized email replies to affected customers.
  Escalation Manager: Ensures high-risk edge cases are properly isolated and directly formatted into structured executive reports.

4. Interactive Dashboards & Deployment (`Task 4`)
  FastAPI Backend: Exposes the orchestration graph as high-performance endpoints.
  Unified Streamlit Interface: Offers four functional views from a single viewport:
  1. EDA Dashboard for overall operation health metrics.
  2. Real-time ANN Classifier playground.
  3. RAG Search Assistant for policy lookups.
  4. Agentic Workflow Trace to inspect LangGraph execution logs.
  Docker Containerization: Includes modular configuration via `docker-compose.yml` to orchestrate service microstructures on independent virtual ports.

---

How to Run

### Local Installation
Ensure you have the required dependencies from `requirements.txt` installed:
```bash
pip install -r requirements.txt
