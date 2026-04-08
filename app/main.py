from fastapi import FastAPI
from app.api import chat,upload
app = FastAPI()



app.include_router(upload.router,prefix= "/upload")
app.include_router(chat.router, prefix= "/chat")
@app.get("/")
def root():
    return {"Api is running"}