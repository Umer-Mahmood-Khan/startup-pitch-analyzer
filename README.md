# 🚀 Startup Pitch Analyzer

A smart tool to analyze your startup idea using **HyDE (Hypothetical Document Embeddings)** + LLMs, then match it to startup categories using **FAISS** vector search.

![App Screenshot](screenshots/ui-demo.png)

---

## 🧠 What is HyDE?

Traditional **RAG (Retrieval-Augmented Generation)** retrieves documents based on similarity to the **question**, which often leads to irrelevant content.

**HyDE**, on the other hand:
- Generates a **hypothetical answer** using an LLM
- Embeds that hypothetical answer
- Retrieves documents similar to that answer, **not just the question**

🔎 This dramatically improves **context relevance**, especially when the original query is vague.

![HyDE vs RAG](screenshots/hyde-vs-rag.gif)

---

## 🎯 Features

- Generate **market summaries** from a 1-liner startup idea
- Extract **SWOT-style** insights
- Match to top startup **categories** using FAISS
- Interactive and **responsive** Streamlit UI
- Uses a **local LLM** (e.g., LLaMA 3) — no API needed!

---

## 💻 How to Run Locally

```bash
git clone https://github.com/yourname/startup-pitch-analyzer.git
cd startup-pitch-analyzer
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
