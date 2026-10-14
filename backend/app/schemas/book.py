from datetime import datetime

from pydantic import BaseModel, ConfigDict


class BookResponse(BaseModel):
    id: int
    library_id: int
    book_code: str
    title: str
    author: str | None
    publisher: str | None
    category: str | None
    isbn: str | None
    total_copies: int
    available_copies: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

from pydantic import BaseModel, ConfigDict


class BookCreate(BaseModel):
    library_id: int
    book_code: str
    title: str
    author: str | None = None
    publisher: str | None = None
    category: str | None = None
    isbn: str | None = None
    total_copies: int = 1


class BookUpdate(BaseModel):
    book_code: str | None = None
    title: str | None = None
    author: str | None = None
    publisher: str | None = None
    category: str | None = None
    isbn: str | None = None
    total_copies: int | None = None