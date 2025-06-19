import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Use a general-purpose embedding model for startup/business text
model_name = "all-MiniLM-L6-v2"
model = SentenceTransformer(model_name)

# 🔹 Batch embedding function
def embed_documents(documents):
    print(f"🧠 [Embedding] Converting {len(documents)} document(s) to vector embeddings...")
    embeddings = model.encode(documents, convert_to_tensor=False)
    return embeddings

# 🔹 Single text embedding for runtime user input
def embed_text(text):
    return model.encode([text])[0]

# 🔹 Build FAISS index (from pre-generated embeddings)
def build_faiss_index(embeddings):
    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype("float32"))
    return index

# 🔹 Save/Load Index
def save_faiss_index(index, path):
    faiss.write_index(index, path)

def load_faiss_index(path):
    return faiss.read_index(path)

# 🔹 Search
def find_closest_category(text, index, labels, top_k=3):
    vector = embed_text(text).astype("float32")
    D, I = index.search(np.array([vector]), k=top_k)
    return [(labels[I[0][i]], D[0][i]) for i in range(top_k)]

