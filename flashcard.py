import spacy
import numpy as np
import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# ✅ Use only PyTorch-based SentenceTransformer
def load_embedder():
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    try:
        return SentenceTransformer(model_name)
    except Exception as e:
        raise Exception(f"Failed to load model: {e}")

def preprocess_text(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    sentences = [sent.text.strip() for sent in doc.sents if sent.text.strip()]
    return sentences

def determine_flashcard_count(text):
    word_count = len(text.split())
    if word_count < 100:
        return 3
    elif 100 <= word_count < 300:
        return 5
    elif 300 <= word_count < 600:
        return 7
    else:
        return 10

def generate_flashcards(text):
    num_flashcards = determine_flashcard_count(text)
    sentences = preprocess_text(text)

    if not sentences:
        return {}

    # ✅ Use only PyTorch model
    model = load_embedder()
    embeddings = model.encode(sentences)
    similarity_matrix = cosine_similarity(embeddings)

    graph = nx.from_numpy_array(similarity_matrix)
    scores = nx.pagerank(graph)

    ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)

    selected = []
    used_phrases = set()

    for _, sentence in ranked_sentences:
        if len(selected) >= num_flashcards:
            break
        cleaned = sentence.strip()
        if cleaned and cleaned not in used_phrases:
            trimmed = '. '.join(cleaned.split('. ')[:3]).strip()
            if not trimmed.endswith('.'):
                trimmed += '.'
            selected.append(trimmed)
            used_phrases.add(trimmed)

    summarized_flashcards = selected
    flashcards = {f"Point {i+1}": point for i, point in enumerate(summarized_flashcards)}
    return flashcards

def get_flashcard_word_count(flashcards):
    return sum(len(card.split()) for card in flashcards.values())
