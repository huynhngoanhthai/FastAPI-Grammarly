# from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

from spelling import spellcheck,addNewWord
app = FastAPI()
class Item(BaseModel):
    content: str
    word: str

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/")
def spelling(item: Item):
    return spellcheck(item.content)
@app.post("/addNewWord")
def addNewWord(item: Item):
    return addNewWord(item.word)