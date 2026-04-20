from langchain_community.vectorstores import FAISS
from langchain_core.embeddings import Embeddings
import numpy as np

class SimpleEmbeddings(Embeddings):
    def embed_documents(self, texts):
        embeddings = []
        for text in texts:
            hash_val = hash(text)
            np.random.seed(abs(hash_val) % (2**32))
            embedding = np.random.rand(384).astype(np.float32)
            embeddings.append(embedding.tolist())
        return embeddings

    def embed_query(self, text):
        hash_val = hash(text)
        np.random.seed(abs(hash_val) % (2**32))
        return np.random.rand(384).astype(np.float32).tolist()

def create_vector_store(chunks):
    embeddings = SimpleEmbeddings()
    vector_store = FAISS.from_documents(chunks, embeddings)
    return vector_store