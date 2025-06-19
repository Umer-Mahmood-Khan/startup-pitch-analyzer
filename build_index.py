from categories_data import get_all_examples_and_labels
from hyde_generator import generate_analysis
from embedder import embed_documents, build_faiss_index, save_faiss_index

import os

# Output paths
INDEX_PATH = "data/faiss_index.bin"
LABELS_PATH = "data/labels.txt"

def main():
    print("🚀 Starting FAISS index creation...")

    examples, labels = get_all_examples_and_labels()

    # Step 1: Generate HyDE outputs for each idea
    hyde_texts = []
    for idea in examples:
        print(f"📝 Generating analysis for: {idea}")
        analysis = generate_analysis(idea)
        hyde_texts.append(analysis)

    # Step 2: Embed each analysis
    embeddings = embed_documents(hyde_texts)

    # Step 3: Build FAISS index
    index = build_faiss_index(embeddings)

    # Step 4: Save index
    os.makedirs("data", exist_ok=True)
    save_faiss_index(index, INDEX_PATH)

    # Step 5: Save category labels
    with open(LABELS_PATH, "w") as f:
        for label in labels:
            f.write(label + "\n")

    print(f"✅ Index saved to {INDEX_PATH}")
    print(f"✅ Labels saved to {LABELS_PATH}")

if __name__ == "__main__":
    main()
