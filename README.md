# 🧠 Smart Flashcard Generator

The **Smart Flashcard Generator** is an AI-powered application built with Python and Streamlit that allows users to generate concise, informative flashcards from large blocks of study text or from images containing text (OCR). It uses Natural Language Processing (NLP) and modern language models to automatically summarize key points and convert them into study-ready flashcards.

---

## 📌 Features

- ✍️ Accepts input as plain **text** or as **images containing text**
- 🧠 Generates **summarized flashcards** using sentence embeddings and graph ranking (PageRank)
- 🔁 **Flip card animation** for an interactive learning experience
- 🔊 Integrated **text-to-speech** to read out flashcard content
- 📈 Real-time statistics: Word count, card count, total sessions, etc.
- 📦 Modular codebase (organized into multiple reusable Python files)
- 🎨 Styled with custom **CSS** for a modern UI

---

## 🚀 Technologies Used

- **Python 3.9+**
- **Streamlit** – for building the web app UI
- **spaCy** – for sentence segmentation and preprocessing
- **transformers + sentence-transformers** – for embedding and semantic understanding
- **NetworkX** – to apply PageRank for identifying important sentences
- **scikit-learn** – for cosine similarity
- **OpenCV (cv2)** + **Tesseract OCR** – for extracting text from images
- **pyttsx3** – for offline text-to-speech

---

## 📂 Project Structure

```
Flashcard_Generator/
│
├── app.py                     # Main Streamlit app
├── flashcard.py               # Flashcard generation logic
├── image_processing.py        # OCR logic using OpenCV & Tesseract
├── text_to_speech.py          # Converts text to speech
├── styles.css                 # Custom CSS styling
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation (this file)
```

---

## ⚙️ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Flashcard_Generator.git
cd Flashcard_Generator
```

### 2. Set Up Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
```

### 3. Install Requirements

```bash
pip install --upgrade pip
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 4. Run the App

```bash
streamlit run app.py
```

Then open your browser to: `http://localhost:8501`

---
