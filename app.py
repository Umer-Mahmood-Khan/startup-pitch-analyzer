import os
os.environ["STREAMLIT_WATCHER_DISABLE"] = "true"

import streamlit as st
from hyde_generator import generate_analysis
from embedder import load_faiss_index, find_closest_category
import pandas as pd

# 🔹 Set page config
st.set_page_config(
    page_title="Startup Pitch Analyzer",
    page_icon="🚀",
    layout="wide"
)

# 🔹 Banner Image (must be in the same directory)
st.image("new.gif", use_container_width =True)

# 🔹 Hero Title and Description
st.markdown("""
# 🚀 Startup Pitch Analyzer
Get fast, AI-powered feedback on your startup idea — including SWOT, business type, and more.

---
""")

# Paths
INDEX_PATH = "data/faiss_index.bin"
LABELS_PATH = "data/labels.txt"

# Load index and labels once
index = load_faiss_index(INDEX_PATH)

with open(LABELS_PATH, "r") as f:
    labels = [line.strip() for line in f.readlines()]

# Streamlit UI
user_input = st.text_input("💡 Enter your startup idea (e.g., 'Uber for tutors'):")

if user_input:
    with st.spinner("Analyzing your idea..."):
        analysis = generate_analysis(user_input)
        top_matches = find_closest_category(analysis, index, labels)

    st.subheader("🧠 Full Analysis:")
    st.markdown(analysis)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🏷️ Top Matching Categories:")
        for label, score in top_matches:
            st.write(f"• {label} ({score:.2f})")

    with col2:
        # 🔹 Bar Chart
        chart_labels = [label for label, _ in top_matches]
        chart_scores = [score for _, score in top_matches]

        df = pd.DataFrame({
            "Category": chart_labels,
            "Similarity Score": chart_scores
        })

        st.subheader("📊 Category Similarity")
        st.bar_chart(df.set_index("Category"))

# Optional Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit, FAISS, and a local LLM")
