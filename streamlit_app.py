import os
import re

import faiss
import numpy as np
import streamlit as st
from openai import OpenAI
from sentence_transformers import SentenceTransformer

EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "poolside/laguna-s-2.1:free"
TOP_K = 3

SYSTEM_PROMPT = (
    "You are Rayyan Khan's portfolio assistant. Answer questions about Rayyan Khan — "
    "his background, experience, projects, skills and contact info — using ONLY the context below. "
    "Keep answers short and conversational (2-4 sentences unless detail is asked for). "
    "If the context doesn't contain the answer, say you don't know and suggest emailing rayanuet@gmail.com."
)


@st.cache_resource
def load_rag():
    text = open("knowledge.md").read()
    parts = re.split(r"^## ", text, flags=re.M)
    chunks = []
    for p in parts:
        p = p.strip()
        if p:
            chunks.append("## " + p if not p.startswith("#") else p)
    embedder = SentenceTransformer(EMBED_MODEL)
    emb = embedder.encode(chunks, normalize_embeddings=True).astype("float32")
    index = faiss.IndexFlatIP(emb.shape[1])
    index.add(emb)
    return chunks, embedder, index


def get_client():
    key = st.secrets.get("OPENROUTER_API_KEY") or os.environ.get("OPENROUTER_API_KEY")
    if not key:
        return None
    return OpenAI(base_url="https://openrouter.ai/api/v1", api_key=key)


def retrieve(question, chunks, embedder, index):
    q = embedder.encode([question], normalize_embeddings=True).astype("float32")
    _, idx = index.search(q, TOP_K)
    return [chunks[i] for i in idx[0]]


def answer(question, chunks, embedder, index, client):
    if client is None:
        return (
            "The chat model isn't configured yet — the owner needs to add the "
            "OPENROUTER_API_KEY secret. Meanwhile, here's the most relevant bit I found:\n\n"
            + retrieve(question, chunks, embedder, index)[0][:600]
        )
    context = "\n\n".join(retrieve(question, chunks, embedder, index))
    try:
        resp = client.chat.completions.create(
            model=LLM_MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"},
            ],
            max_tokens=300,
            temperature=0.3,
        )
        return resp.choices[0].message.content
    except Exception as e:
        return f"Sorry, the language model hit an error ({type(e).__name__}). Please try again in a moment."


st.set_page_config(page_title="Chat with Rayyan Khan's Portfolio", page_icon="💬")
st.title("Chat with Rayyan Khan's Portfolio")
st.write(
    "A retrieval-augmented chatbot over Rayyan Khan's portfolio — ML Engineer from Mardan, Pakistan. "
    "Ask about his projects, experience, skills, or how to contact him."
)

chunks, embedder, index = load_rag()
client = get_client()

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if question := st.chat_input("Ask about Rayyan's work, skills, experience..."):
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            reply = answer(question, chunks, embedder, index, client)
        st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
