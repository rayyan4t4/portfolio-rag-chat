# About Rayyan Khan

Rayyan Khan is a Machine Learning Engineer based in Mardan, Khyber Pakhtunkhwa, Pakistan. He is a final-year BS Computer Science student at UET Mardan (2023–2027, CGPA 3.63/4.00) and the Machine Learning Team Lead at ITSimplera Solutions (2026–present).

He describes himself as "engineer first, researcher by habit." His foundation is applied machine learning, and he is deliberately building upward into generative AI — transformers, LLM APIs, embeddings, RAG, fine-tuning and agents — through 45 focused minutes of daily study.

## Experience

**Machine Learning Team Lead @ ITSimplera Solutions (2026–present):** Leads the ML team, setting technical direction for model work and reviewing what the team builds. Hands-on across client projects: data preparation, training, evaluation, and getting results into a usable state. Mentors juniors on PyTorch and code quality.

**Machine Learning Intern @ CodeClub, Peshawar (Jul 2025):** Collected and organised real-world datasets for object detection and classification. Labelled data in CVAT, checked it for consistency, removed duplicates and balanced classes before training.

**BS Computer Science @ UET Mardan (2023–2027):** Final-year student, CGPA 3.63/4.00. Dean's Appreciation Award, 2025.

## Projects

### Ask the Constitution
RAG chatbot over the Constitution of Pakistan — ask questions in plain language, get answers grounded in the actual articles with citations. Corpus: 323 articles (numbers 1–280 complete) + 5 schedules scraped from pakistani.org; retrieval with all-MiniLM-L6-v2 embeddings + FAISS (768 chunks). Evaluated on 30 hand-written questions with gold article labels: hit-rate@1 0.867, hit-rate@3 0.933, hit-rate@5 1.000. Try it live: https://ask-the-constitution-pakistan-4qnovtlwn9uu6gw5qry8nw.streamlit.app/ (shows retrieved articles with citations; full generated answers need the OpenRouter API key in the app's secrets). Source code: https://github.com/rayyan4t4/ask-the-constitution-pakistan. Built with sentence-transformers, FAISS and Streamlit. Day 3 of his daily ML project series — his first RAG system.

### Roman Urdu Sentiment Analyzer
Sentiment analysis for Roman Urdu text — TF-IDF + logistic regression trained on 33,619 labeled texts (Positive/Negative/Neutral). Test macro-F1 0.689 against a 0.216 majority-class baseline on 4,151 held-out rows. Try it live: https://roman-urdu-sentiment-analyzer-wgx8edlhcfylauqebaacbb.streamlit.app/ (type any Roman Urdu, get sentiment plus confidence). Source code: https://github.com/rayyan4t4/roman-urdu-sentiment-analyzer. Built with scikit-learn and Streamlit. His first NLP project, day 2 of the daily ML project series.

### Lahore Smog Forecast
24-hour PM2.5 forecasting for Lahore with a 2-layer LSTM (64 hidden units, 72-hour lookback). Trained on 4 years of hourly pollution + weather data (41,832 rows, Open-Meteo/CAMS). Test MAE 17.72 vs persistence baseline 24.20 (27% better) on 15,433 held-out hours. Live Streamlit dashboard. Built with PyTorch and Streamlit.

### Conformer Speech Enhancement
Single-channel noise suppression with a Conformer encoder using complex ratio masking over magnitude and phase. Evaluated with PESQ, STOI and SI-SDR. Trains on free-tier hardware. Built with PyTorch and torchaudio.

### PDF AI Authorship Analyzer
Batch-scores text PDFs with a 0–100 AI-authorship risk score computed from five signals. Runs fully locally so documents never leave the machine. Built with Python, Streamlit and Transformers.

### Fire & Weapon Detection from CCTV
Team project detecting fire and weapons in live CCTV footage. No dataset existed, so the team built one — around 8,000 frames annotated in CVAT — and reached 0.89 mAP@0.5 with YOLO. Built with YOLO, OpenCV and PyTorch.

### Veterinary RAG Assistant
Retrieval-augmented decision-support assistant over veterinary knowledge. Built with LangChain, FAISS and LLMs.

### LLM + RAG Experiments
Hands-on notebooks covering embeddings, vector stores, chunking strategies and retrieval evaluation. Built with LlamaIndex and ChromaDB.

### Word-AI
An AI task-pane add-in for Microsoft Word — write, edit and format documents with an assistant inside the editor. Built with Python and LLM APIs.

### Portfolio RAG Chatbot (this app)
A retrieval-augmented chatbot over Rayyan's own portfolio. Ask it anything about his work, skills and experience. Built with Streamlit, sentence-transformers, FAISS and an OpenRouter-hosted LLM.

## Skills

Working knowledge: Python, PyTorch, scikit-learn, Hugging Face, OpenCV, YOLO, Streamlit, FastAPI, NumPy, pandas, SQL, Git & GitHub, Docker, Linux, CVAT, Bash, C/C++.

Currently learning: LLMs, RAG, LangChain, LlamaIndex, AI agents, MCP, FAISS, ChromaDB, LoRA, prompt engineering.

His GenAI learning roadmap (45 minutes a day): 1. PyTorch refresh (done), 2. Transformers inside-out (in progress), 3. LLM APIs in production, 4. Embeddings & vector DBs, 5. RAG systems, 6. LoRA fine-tuning, 7. Agents & MCP, 8. Portfolio builds.

## Credentials

- AI Agents 101 — Building AI Agents with MCP & Open-Source Inference
- Retrieval-Augmented Generation for Production — LangChain & LlamaIndex
- Programming Competition Award — AWKUM Garden Campus, 2025
- Dean's Appreciation Award — UET Mardan, 2025

## Contact

Email: rayanuet@gmail.com. GitHub: github.com/rayyan4t4. LinkedIn: linkedin.com/in/rayyanstein. Portfolio: rayyankhan.online. He is open to work — ML roles, freelance model training and system builds.
