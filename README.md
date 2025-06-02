
# 🚀 ChatSleuth



ChatSleuth is a chat search engine that replicates WhatsApp’s in-chat keyword search and highlighting feature. It enables users to quickly find and visually highlight specific words within chat conversations, delivering fast and efficient search results even across large datasets.

---

## ✨ Features

- **🔎 Efficient Search:** Uses an **Inverted Index** data structure to quickly locate messages containing the queried words without scanning the entire chat history.  
- **💡 Word Highlighting:** Implements the **Knuth-Morris-Pratt (KMP) algorithm** for fast and accurate pattern matching to highlight search keywords within messages.  
- **📈 Scalable:** Designed to handle large volumes of chat data with minimal latency.

---

## 🧠 How It Works

### 📚 Inverted Index

An inverted index maps each word to the list of messages where it appears, much like the index at the back of a book. This allows ChatSleuth to jump directly to relevant messages instead of scanning all data.

### ⚡ KMP Algorithm

For highlighting, a naive approach could take **O(m·n)** time (where *m* is the pattern length and *n* is the text length). Using the KMP algorithm optimizes this to **O(m + n)**, significantly speeding up keyword highlighting within messages.

---

## 🌐 Demo

Try out the live demo here: [https://chatbotwithdeepali.onrender.com](https://chatbotwithdeepali.onrender.com)

---


## 🚀 Usage

* Enter your search query in the search bar.
* Relevant messages containing the keyword(s) will be retrieved instantly.
* Search terms will be highlighted within the chat messages.

---

## 🧩 Technologies Used

* Data Structures: Inverted Index
* Algorithms: Knuth-Morris-Pratt (KMP)
* Programming Languages: Python, JavaScript
* Markup & Styling: HTML, CSS, Bootstrap



