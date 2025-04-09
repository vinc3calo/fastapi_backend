from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

books = []  # in-memory database

class Post(BaseModel):
    title: str
    content: str
    created_at: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Post API!"}

@app.get("/books", response_model=List[Book])
def get_books():
    return books

@app.post("/books", response_model=Book)
def add_book(book: Book):
    books.append(book)
    return book
