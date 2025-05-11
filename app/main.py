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


    


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from flask import Flask, render_template, request, jsonify
import nltk
from utils.text_preprocessing import text_preprocess
from core.index_builder import inverted_index_builder
from core.query_handler import word_search

# Ensure NLTK data is available
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')

app = Flask(__name__, static_folder="../static", template_folder="../templates")

with open("data/chat_history.txt", "r", encoding="utf-8", errors="ignore") as file:
    raw_messages = file.readlines()

cleaned_messages = [text_preprocess(msg.strip()) for msg in raw_messages]
inverted_index = inverted_index_builder(cleaned_messages)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()
    query = data.get("query", "")
    if not query.strip():
        return jsonify({"results": []})
    line_indexes = word_search(query, inverted_index)
    results = [raw_messages[i].strip() for i in sorted(line_indexes)]
    return jsonify({"results": results})

if __name__ == "__main__":
    app.run(debug=True)
