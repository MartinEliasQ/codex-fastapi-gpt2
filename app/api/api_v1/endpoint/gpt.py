from fastapi import APIRouter
from gpt.predict import predict


router = APIRouter()
@router.post("/")
def generate_text(*, message: str):
    response = predict(sentence=message)
    return response

