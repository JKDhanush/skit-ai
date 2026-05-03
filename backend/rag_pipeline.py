from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Always be polite and non-threatening.",
    "Offer payment plans if user shows difficulty.",
    "Never use abusive or coercive language.",
    "Remind users of due dates clearly."
]

doc_embeddings = model.encode(documents)
index = faiss.IndexFlatL2(doc_embeddings.shape[1])
index.add(np.array(doc_embeddings))

def retrieve_context(query):
    query_embedding = model.encode([query])
    D, I = index.search(query_embedding, k=2)
    return [documents[i] for i in I[0]]
