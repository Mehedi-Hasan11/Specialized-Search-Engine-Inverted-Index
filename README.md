# 🔍 LexendSearch Academic: Specialized Research Paper Search Engine

A specialized, high-performance information retrieval (IR) search engine built completely from scratch using a custom **Inverted Index** architecture and **TF-IDF ranking**. This platform specifically indexes and queries academic data derived from the ArXiv Machine Learning repository.

⭐ **Bonus Feature:** Implements a modern, responsive Web Graphical User Interface (GUI) engineered using Streamlit, featuring real-time dynamic keyword highlighting.

---

## 👥 Authors
* **Mehedi Hasan** (ID: `0432220005101033`)
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


---

## 💻 Installation & Local Execution Setup

### 1. Prerequisites
Ensure you have Python installed on your local computer system (Recommended version `Python 3.10` or above).

### 2. Clone the Repository
```bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/Specialized-Search-Engine-Inverted-Index.git](https://github.com/Mehedi/Specialized-Search-Engine-Inverted-Index.git)
cd Specialized-Search-Engine-Inverted-Index
3. Install Package Dependencies
Install the verified libraries required for structural formatting and preprocessing:

Bash
pip install streamlit nltk pandas numpy
(If you are on Windows and experience command path errors, try running: python -m pip install streamlit nltk pandas numpy)

4. Running the Web GUI Application
Launch the web interface presentation server using the local streamlit runner:

Bash
streamlit run app.py
📁 Repository Structure
├── engine.py          # Core Information Retrieval Engine & Custom Inverted Index Matrix
├── app.py             # Streamlit Modern Web Graphical User Interface Layout & Rendering
├── README.md          # Comprehensive Project Architectural Run Documentation
└── arxiv_data.csv     # Research Paper dataset parsed via Kaggle Snapshots
🔬 Sample Target Search Queries to Test
Once the interface opens up in your default web browser, try testing the indexing pipeline using these highly dense academic terms:

neural networks (Use OR (Flexible) strategy)

quantum algorithms

stochastic optimization parameters
