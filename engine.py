import math
import re
import os
from collections import defaultdict

import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# -----------------------------------
# DOWNLOAD NLTK DATA
# -----------------------------------

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")


class SpecializedSearchEngine:

    def __init__(self):

        # term -> {doc_id: frequency}
        self.index = defaultdict(dict)

        # document storage
        self.documents = {}

        # document lengths
        self.doc_lengths = {}

        # total documents
        self.N = 0

        # stopwords + stemmer
        try:
            self.stop_words = set(stopwords.words("english"))
        except:
            self.stop_words = set()

        self.stemmer = PorterStemmer()

    # -----------------------------------
    # PREPROCESSING
    # -----------------------------------
    def _preprocess(self, text):

        text = str(text).lower()
        text = re.sub(r"[^\w\s]", " ", text)
        tokens = text.split()

        tokens = [
            self.stemmer.stem(token)
            for token in tokens
            if token not in self.stop_words
        ]

        return tokens

    # -----------------------------------
    # ADD DOCUMENT
    # -----------------------------------
    def add_document(self, doc_id, title, content):

        self.documents[doc_id] = {
            "title": title,
            "content": content
        }

        tokens = self._preprocess(title + " " + content)

        self.doc_lengths[doc_id] = max(len(tokens), 1)

        term_counts = defaultdict(int)

        for token in tokens:
            term_counts[token] += 1

        for term, freq in term_counts.items():
            self.index[term][doc_id] = freq

        self.N += 1

    # -----------------------------------
    # IDF
    # -----------------------------------
    def _get_idf(self, term):

        df = len(self.index.get(term, {}))

        if df == 0:
            return 0

        return math.log10((self.N / df) + 1)

    # -----------------------------------
    # BOOLEAN SEARCH
    # -----------------------------------
    def boolean_search(self, query, mode="AND"):

        tokens = self._preprocess(query)

        if not tokens:
            return set()

        matching_docs = [
            set(self.index.get(token, {}).keys())
            for token in tokens
        ]

        if not matching_docs:
            return set()

        if mode == "AND":
            return set.intersection(*matching_docs)

        return set.union(*matching_docs)

    # -----------------------------------
    # TF-IDF SEARCH
    # -----------------------------------
    def search(self, query, mode="OR"):

        tokens = self._preprocess(query)

        if not tokens:
            return []

        candidate_docs = self.boolean_search(query, mode=mode)

        scores = defaultdict(float)

        for token in tokens:

            idf = self._get_idf(token)

            if idf == 0:
                continue

            postings = self.index.get(token, {})

            for doc_id in candidate_docs:

                if doc_id not in postings:
                    continue

                tf = postings[doc_id]

                tf_weight = 1 + math.log10(tf) if tf > 0 else 0

                doc_len = self.doc_lengths.get(doc_id, 1)

                scores[doc_id] += (tf_weight * idf) / doc_len

        ranked_docs = sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        results = []

        for doc_id, score in ranked_docs:

            doc = self.documents[doc_id]
            content = doc["content"]

            pos = content.lower().find(tokens[0].lower())

            if pos != -1:
                start = max(0, pos - 100)
                end = min(len(content), pos + 250)
                snippet = content[start:end]
            else:
                snippet = content[:250]

            if len(content) > 250:
                snippet += "..."

            results.append({
                "doc_id": doc_id,
                "title": doc["title"],
                "snippet": snippet,
                "score": round(score, 4),
            })

        return results


# -----------------------------------
# LOAD DATASET
# -----------------------------------

def load_sample_dataset(engine):

    file_path = r"D:\Specialized-Search-Engine-Inverted-Index\dataset\arXiv_scientific dataset.csv"

    if not os.path.exists(file_path):

        print("⚠️ Dataset not found:", file_path)

        engine.add_document(
            1,
            "Dataset Missing",
            "Please check dataset path."
        )

        return

    try:

        df = pd.read_csv(
            file_path,
            encoding="utf-8",
            low_memory=False
        )

        sample_df = df.head(5000)

        for idx, row in sample_df.iterrows():

            doc_id = idx + 1

            title = str(row.get("title", "No Title")).strip()
            content = str(row.get("summary", "No Summary")).strip()

            engine.add_document(doc_id, title, content)

        print(f"✅ Indexed {len(sample_df)} papers successfully.")

    except Exception as e:
        print("❌ Error loading dataset:", e)


# -----------------------------------
# TEST RUN (OPTIONAL)
# -----------------------------------
if __name__ == "__main__":

    engine = SpecializedSearchEngine()
    load_sample_dataset(engine)

    print("\n🔎 Search Results:")
    results = engine.search("machine learning neural network")

    for r in results[:5]:
        print(r)