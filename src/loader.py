from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_documents(file_path):
    # Read text file with UTF-8 encoding
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.create_documents([text])
    return chunks