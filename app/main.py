# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from utils.text_preprocessing import text_preprocess
# from core.inverted_index import inverted_index_builder
# from core.query_handler import word_search

# with open("data/chat_history.txt","r", encoding="utf-8", errors="ignore") as file:
#     raw_messages = file.readlines()

# cleaned_messages = [text_preprocess(msg.strip()) for msg in raw_messages]

# inverted_index = inverted_index_builder(cleaned_messages)

# def main():
    
#     while True:
#         query = input("Enter the word:(press 'exit' to discontinue)").strip()
#         line_idx = word_search(query, inverted_index)
#         if(query.lower() == "exit"):
#             break
#         if(line_idx):
#             for i in sorted(line_idx):
#                 print(f'{i + 1} : {raw_messages[i]}.strip()')
#         else : 
#             print(f"Sorry no messages found for{query}. Try some another word.")

    
   
    

# if(__name__ == "__main__"):
#     main()


    


# 


import sys
import os
import pickle
import nltk
from flask import Flask, render_template, request, jsonify

# Set up paths
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(BASE_DIR)

NLTK_DATA_PATH = os.path.join(BASE_DIR, 'nltk_data')
DATA_PATH = os.path.join(BASE_DIR, 'data', 'chat_history.txt')
INDEX_PATH = os.path.join(BASE_DIR, 'data', 'inverted_index.pkl')

# Ensure NLTK data path exists
os.makedirs(NLTK_DATA_PATH, exist_ok=True)
nltk.data.path.append(NLTK_DATA_PATH)

# Download NLTK resources only if not already present
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', download_dir=NLTK_DATA_PATH)

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', download_dir=NLTK_DATA_PATH)

# Custom imports
from utils.text_preprocessing import text_preprocess
from core.index_builder import inverted_index_builder
from core.query_handler import word_search
from core.highlight import highlight_matches

# Read raw messages
with open(DATA_PATH, "r", encoding="utf-8", errors="ignore") as file:
    raw_messages = file.readlines()

# Build or load inverted index
if os.path.exists(INDEX_PATH):
    with open(INDEX_PATH, 'rb') as f:
        inverted_index = pickle.load(f)
else:
    cleaned_messages = [text_preprocess(msg.strip()) for msg in raw_messages]
    inverted_index = inverted_index_builder(cleaned_messages)
    with open(INDEX_PATH, 'wb') as f:
        pickle.dump(inverted_index, f)

# Initialize Flask app
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
    if not query:
        return jsonify({"results": []})
    
    line_indexes = word_search(query, inverted_index)
    results = [highlight_matches(raw_messages[i].strip(), query) for i in sorted(line_indexes)]
    return jsonify({"results": results})

if __name__ == "__main__":
    app.run(debug=False)  # Use debug=True only during development
