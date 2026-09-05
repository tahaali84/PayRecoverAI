def build_vector_store(documents, embeddings):
    from langchain_community.vectorstores import FAISS
    return FAISS.from_documents(documents, embeddings)
