from langchain_community.document_loaders import PyPDFLoader


def load_pdf(file_path : str):
    print("file path in loader:",str)
    loader =  PyPDFLoader(file_path)
    document = loader.load()
    return document