from fastapi import APIRouter,UploadFile, File
from app.service.document_service import load_pdf
from app.utils.chunking import split_document
import os


router = APIRouter()

Upload_Dir = "storage"
os.makedirs(Upload_Dir,exist_ok=True)

@router.get("/")
def upload():
    return {"Upload Api is alive"}

@router.post("/add")
async def upload_file(file: UploadFile = File(...)):
    
    file_path = os.path.join(Upload_Dir, file.filename)

    content = await file.read()
    print("File size:", len(content))

    with open(file_path, "wb") as buffer:
        buffer.write(content)


    docs = load_pdf(file_path)
    print("Loaded docs:", len(docs))


    chunks = split_document(docs)
    print("Chunks:", len(chunks))

 
    sample = chunks[0].page_content[:500] if chunks else "No content"

    return {
        "filename": file.filename,
        "sample_chunk": sample
    }
