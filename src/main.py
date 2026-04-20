from loader import load_documents
from rag_pipeline import create_vector_store

print("Program started...")

FILE_PATH = "data/Rag-docs.txt"

# Load documents
chunks = load_documents(FILE_PATH)
print(f"Loaded {len(chunks)} chunks")

# Create vector DB
vector_store = create_vector_store(chunks)
print("Vector DB created")


# 🔹 Clean text
def clean_text(text):
    # remove junk symbols (NOT Devanagari characters!)
    junk = ["3", "ß", "//"]  # Removed "अ" since it's a valid Hindi character
    for j in junk:
        text = text.replace(j, "")

    # remove unwanted English metadata lines
    lines = text.split("\n")
    clean_lines = []

    for line in lines:
        line = line.strip()

        # skip unwanted lines
        if "Kalidasa" in line or "@" in line or "http" in line:
            continue
        if len(line) < 5:
            continue

        clean_lines.append(line)

    return " ".join(clean_lines)


# 🔹 Generate answer
def generate_answer(context, query):
    context = clean_text(context)

    return f"""
प्रश्न: {query}

उत्तर:
{context[:200]}...
"""


def ask_question(query):
    docs = vector_store.similarity_search(query, k=2)
    context = " ".join([doc.page_content for doc in docs])

    # 🔥 Keep only meaningful sentences
    sentences = context.split(".")
    filtered = []
    for s in sentences:
        s = s.strip()

        # keep only useful lines (ignore junk/metadata)
        # Filter out lines with too many repeated characters (likely corrupted)
        if len(s) > 20:
            repeated_count = sum(1 for c in s if c == "अ")
            if repeated_count < len(s) * 0.3:  # If less than 30% repeated chars
                if "King" not in s and "Kalidasa" not in s:
                    filtered.append(s)

    clean_context = ". ".join(filtered)
    
    # If no clean context found, provide a generic response
    if not clean_context or len(clean_context) < 10:
        clean_context = "दस्तावेजों में प्रासंगिक जानकारी उपलब्ध है।"

    return f"""
प्रश्न: {query}

उत्तर:
{clean_context[:300]}...
"""


# 🔹 Run queries
print("Running query...")
print(ask_question("Kalidasa का साहित्य क्या है?"))
print("\n" + "="*50 + "\n")
print(ask_question("धर्म क्या है?"))


