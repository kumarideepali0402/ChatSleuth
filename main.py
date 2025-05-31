import sys
import os
import pickle
import nltk
from flask import Flask, render_template, request, jsonify

# --- Setup Paths ---
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

NLTK_DATA_PATH = os.path.join(BASE_DIR, 'nltk_data')
DATA_PATH = os.path.join(BASE_DIR, 'data', 'chat_history.txt')
INDEX_PATH = os.path.join(BASE_DIR, 'data', 'inverted_index.pkl')

# --- Ensure NLTK Downloads Folder Exists ---
os.makedirs(NLTK_DATA_PATH, exist_ok=True)
nltk.data.path.append(NLTK_DATA_PATH)

# --- Download NLTK Data if Not Already Present ---
for resource in ['punkt', 'stopwords']:
    try:
        nltk.data.find(f'tokenizers/{resource}' if resource == 'punkt' else f'corpora/{resource}')
    except LookupError:
        nltk.download(resource, download_dir=NLTK_DATA_PATH)

# --- Custom Imports ---
from utils.text_preprocessing import text_preprocess
from core.index_builder import inverted_index_builder
from core.query_handler import word_search
from core.highlight import highlight_matches

# --- Read and Preprocess Messages ---
with open(DATA_PATH, "r", encoding="utf-8", errors="ignore") as file:
    raw_messages = file.readlines()

if os.path.exists(INDEX_PATH):
    with open(INDEX_PATH, 'rb') as f:
        inverted_index = pickle.load(f)
else:
    cleaned_messages = [text_preprocess(msg.strip()) for msg in raw_messages]
    inverted_index = inverted_index_builder(cleaned_messages)
    with open(INDEX_PATH, 'wb') as f:
        pickle.dump(inverted_index, f)

# --- Initialize Flask ---
app = Flask(
    __name__,
    static_folder=os.path.join(BASE_DIR, 'static'),
    template_folder=os.path.join(BASE_DIR, 'templates')
)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()
    query = data.get("query", "").strip()
    processed_query = text_preprocess(query)

    print("User Query:", query)
    print("Processed Query:", processed_query)

    line_indexes = word_search(processed_query, inverted_index)
    print("Matched lines:", line_indexes)

    if not line_indexes:
        return jsonify({"results": []})

    results = [highlight_matches(raw_messages[i].strip(), query) for i in sorted(line_indexes)]
    return jsonify({"results": results})


# --- Entry Point ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render compatibility
    app.run(debug=False, host="0.0.0.0", port=port)
