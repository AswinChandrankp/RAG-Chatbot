from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def chat_test():
    return {"Chat api is alive"}