# Chat with Rayyan Khan's Portfolio

A retrieval-augmented chatbot over Rayyan Khan's portfolio — portfolio content is chunked and embedded with `all-MiniLM-L6-v2`, retrieved with FAISS, and answered by an LLM via OpenRouter (free tier). Built with Streamlit.

## Setup

Add your OpenRouter API key as a Streamlit secret named `OPENROUTER_API_KEY` (App settings → Secrets):

```toml
OPENROUTER_API_KEY = "sk-or-v1-..."
```

## Run locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```
