from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_document (document):
    spitter = RecursiveCharacterTextSplitter(
             chunk_size=500,
             chunk_overlap=50
    )

    chunks = spitter.split_documents(document)
    return chunks