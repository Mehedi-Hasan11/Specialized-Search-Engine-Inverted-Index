# 🔍 LexendSearch Academic: Specialized Research Paper Search Engine

A specialized, high-performance information retrieval (IR) search engine built completely from scratch using a custom **Inverted Index** architecture and **TF-IDF ranking**. This platform specifically indexes and queries academic data derived from the ArXiv Machine Learning repository.

⭐ **Bonus Feature:** Implements a modern, responsive Web Graphical User Interface (GUI) engineered using Streamlit, featuring real-time dynamic keyword highlighting.

---

## 👥 Authors
* **Mehedi Hasan** (ID: `0432220005101033`)
* **Taposhi Rabia Fardin ** (ID: `0432220005101049`)
* **Department:** Computer Science and Engineering (CSE), UITS

---

## 🚀 Key Features
- **Zero Heavy Search Engines Dependency:** Does NOT use any pre-built query or indexing platforms (such as Elasticsearch, Solr, Lucene, or Whoosh).
- **Custom Inverted Index Pipeline:** Maps complex tokenized roots down to structured occurrences matrix (`term -> { document_id: term_frequency }`).
- **NLTK Preprocessing Lifecycle:** Implements full textual pipeline including punctuation clearing, case-folding, stop-word elimination, and Porter Stemming.
- **Boolean & Relational Operations:** Supports advanced query parsing modes:
  - `AND (Strict Retrieval)`: Computes intersections across postings groups ($P_1 \cap P_2$).
  - `OR (Flexible Retrieval)`: Computes global unions ($P_1 \cup P_2$).
- **Vector Space Matrix Ranking:** Evaluates search results sorting using continuous TF-IDF weighting equations with smooth document frequency logs.

---

## 📊 Dataset Specifications
The search engine processes data curated from the Kaggle Dataset: **Research Paper Recommendation (`harshsingh2209/research-paper-recommendation`)**. 

The system maps and ingests the following structured primary parameters:
* `title`: Structural meta-string containing titular research names.
* `abstract`: Rich text corpus detailing deep technical methodology and experimental logs.
* `year`: Publication timestamp for relational verification.

---

## 🛠️ System Architecture & Workflow

[Raw Document Database]
│
▼ (Punctuation Stripping & Case Normalization)
[Cleaned Token Stream]
│
▼ (Stop-words Filtering & Porter Stemming)
[Stemmed Vector Roots]
│
▼
[Custom Inverted Index Structure] ───► Map: { term: { doc_id: term_frequency } }
│
▼ (User Query Processing)
[TF-IDF Log Scoring Matrix] ───► Equation: (1 + log10(tf)) * log10(N/df + 1)
│
▼
[Lexend UI Ranked Presentation Layer] (Highest relevance items highlighted)
