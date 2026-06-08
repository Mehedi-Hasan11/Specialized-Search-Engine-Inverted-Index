import re
import streamlit as st
from engine import SpecializedSearchEngine, load_sample_dataset

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Specialized Search Engine",
    page_icon="🔍",
    layout="wide"
)

# -----------------------------------
# CUSTOM CSS
# -----------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Lexend:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Lexend', sans-serif;
}

.main-title {
    text-align:center;
    color:#1a88c8;
    font-weight:700;
    margin-bottom:5px;
}

.sub-title {
    text-align:center;
    color:#666;
    margin-bottom:25px;
}

.result-card {
    padding:18px;
    border-radius:10px;
    border-left:6px solid #1a88c8;
    background-color:#f8f9fa;
    margin-bottom:15px;
}

.highlight {
    background-color:#fff176;
    padding:2px;
    border-radius:3px;
    font-weight:bold;
}

.score-badge {
    color:#1a88c8;
    font-weight:600;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# LOAD ENGINE
# -----------------------------------

if "engine" not in st.session_state:
    engine = SpecializedSearchEngine()
    load_sample_dataset(engine)
    st.session_state.engine = engine

# -----------------------------------
# HEADER
# -----------------------------------

st.markdown(
    """
    <h1 class='main-title'>
    🔍 Specialized Search Engine using Inverted Index
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class='sub-title'>
    Research Paper Search Engine using TF-IDF Ranking & Inverted Index
    <br><br>
    <b>Developed By:</b> Mehedi Hasan
    <br>
    <b>ID:</b> 0432220005101033
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# -----------------------------------
# SEARCH CONTROLS
# -----------------------------------

query = st.text_input(
    "Search Research Papers",
    placeholder="Example: machine learning, neural networks, transformers"
)

col1, col2 = st.columns(2)

with col1:
    mode = st.selectbox(
        "Boolean Retrieval Mode",
        ["OR (Flexible)", "AND (Strict)"]
    )

with col2:
    st.info(
        "Tip: Use multiple keywords for better results."
    )

# -----------------------------------
# SEARCH EXECUTION
# -----------------------------------

if query:

    query_upper = query.upper()

    if " AND " in query_upper:
        boolean_mode = "AND"
        query = query_upper.replace("AND", " ")

    elif " OR " in query_upper:
        boolean_mode = "OR"
        query = query_upper.replace("OR", " ")

    else:
        boolean_mode = "OR" if "OR" in mode else "AND"

    results = st.session_state.engine.search(
        query,
        mode=boolean_mode
    )

    st.success(
        f"Found {len(results)} relevant document(s)"
    )

    st.markdown("---")

    if results:

        for res in results:

            title_display = res["title"]
            snippet_display = res["snippet"]

            for word in query.split():

                if len(word) > 2:

                    pattern = re.compile(
                        re.escape(word),
                        re.IGNORECASE
                    )

                    title_display = pattern.sub(
                        f"<span class='highlight'>{word}</span>",
                        title_display
                    )

                    snippet_display = pattern.sub(
                        f"<span class='highlight'>{word}</span>",
                        snippet_display
                    )

            st.markdown(
                f"""
                <div class="result-card">

                    <h3 style="margin-bottom:8px;color:#1a88c8;">
                        {title_display}
                    </h3>

                    <p>
                        <span class="score-badge">
                            Relevance Score:
                        </span>
                        {res['score']}
                        &nbsp;&nbsp;|&nbsp;&nbsp;
                        <span class="score-badge">
                            Document ID:
                        </span>
                        {res['doc_id']}
                    </p>

                    <p style="color:#333;">
                        {snippet_display}
                    </p>

                </div>
                """,
                unsafe_allow_html=True
            )

    else:

        st.warning(
            "No matching research papers found. Try different keywords."
        )

# -----------------------------------
# FOOTER
# -----------------------------------

st.divider()

st.caption(
    "Specialized Search Engine using Inverted Index | UITS Assignment Project"
)