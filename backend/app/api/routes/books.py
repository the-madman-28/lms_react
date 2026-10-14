from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import SessionLocal
from app.schemas.book import BookResponse
from app.services.book_service import get_books
from fastapi import APIRouter, Depends, HTTPException, status
from app.services.book_service import get_book, get_books


router = APIRouter(
    prefix="/api/books",
    tags=["Books"],
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.get(
    "/",
    response_model=list[BookResponse],
)
def list_books(
    library_id: int,
    db: Session = Depends(get_db),
):
    return get_books(
        db=db,
        library_id=library_id,
    )


@router.get(
    "/{book_id}",
    response_model=BookResponse,
)
def get_single_book(
    book_id: int,
    library_id: int,
    db: Session = Depends(get_db),
):
    book = get_book(
        db=db,
        library_id=library_id,
        book_id=book_id,
    )

    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )

    return book