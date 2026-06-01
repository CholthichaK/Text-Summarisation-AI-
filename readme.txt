# 📝 Text Summarization AI

A web-based AI text summarization application built with **FastAPI**, **Streamlit**, and **Hugging Face Transformers**. The system allows users to input long articles, reports, or paragraphs and automatically generate concise summaries using the **facebook/bart-large-cnn** summarization model.

---

## 📌 Project Overview

Reading lengthy documents can be time-consuming. This project uses Natural Language Processing (NLP) techniques to automatically extract the key information from a text and generate a shorter, meaningful summary.

The application consists of:

* **FastAPI Backend** for handling summarization requests
* **Hugging Face Transformers** for AI-powered summarization
* **Streamlit Frontend** for an interactive user interface
* **Text Preprocessing Module** for cleaning and preparing input text

---

## 🚀 Features

* Generate summaries from long text passages
* Adjustable minimum and maximum summary lengths
* Automatic text cleaning and preprocessing
* RESTful API built with FastAPI
* User-friendly Streamlit interface
* Uses a state-of-the-art Transformer model (BART)

---

## 🛠 Technologies Used

### Backend

* Python
* FastAPI
* Pydantic
* Uvicorn

### NLP & Machine Learning

* Hugging Face Transformers
* Facebook BART Large CNN
* PyTorch

### Frontend

* Streamlit
* Requests

---

## 📂 Project Structure

```text
text summarization ai/
│
├── app/
│   ├── main.py
│   ├── schemas.py
│   ├── summarizer.py
│   └── preprocessing.py
│
├── frontend/
|   ├── streamlit_app.py
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/text-summarization-ai.git
cd text-summarization-ai
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

### Start the FastAPI Backend

```bash
uvicorn app.main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

### Start the Streamlit Frontend

Open another terminal and run:

```bash
streamlit run streamlit_app.py
```

The web application will open automatically in your browser.

---

## 📡 API Endpoints

### GET /

Returns a welcome message.

**Response**

```json
{
  "message": "Welcome to the Text Summarization API"
}
```

---

### GET /models

Returns available summarization models.

**Response**

```json
{
  "available_models": [
    "facebook/bart-large-cnn"
  ],
  "default_model": "facebook/bart-large-cnn"
}
```

---

### POST /summarize

Generates a summary from the provided text.

#### Request

```json
{
  "text": "Artificial Intelligence is transforming industries...",
  "max_summary_length": 130,
  "min_summary_length": 30
}
```

#### Response

```json
{
  "original_text": "Artificial Intelligence is transforming industries...",
  "summary": "AI is transforming industries by improving efficiency and decision-making."
}
```

---

## 🧹 Text Preprocessing

Before summarization, the system performs:

1. Removal of extra spaces, tabs, and line breaks
2. Text normalization
3. Sentence case conversion
4. Input truncation (default: 500 words)

This preprocessing improves model performance and reduces unnecessary noise.

---

## 🤖 Summarization Model

The project uses:

**facebook/bart-large-cnn**

BART (Bidirectional and Auto-Regressive Transformer) is a transformer-based sequence-to-sequence model trained for text generation and summarization tasks.

Advantages:

* High-quality abstractive summaries
* Strong performance on news articles and reports
* Easy integration through Hugging Face Transformers

---

## 📷 User Interface

The Streamlit application provides:

* Text input area
* Adjustable summary length sliders
* Summary generation button
* Display of original text and generated summary

---

## 🔮 Future Improvements

* Support multiple summarization models
* Upload PDF and DOCX files
* Export summaries as PDF
* Summary quality evaluation metrics
* Keyword extraction
* Multi-language summarization
* Deploy using Docker and Cloud Services

---

