from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.book import Book
from app.models.book_transaction import BookTransaction
from app.models.book import Book


def get_books(
    db: Session,
    library_id: int,
) -> list[Book]:
    statement = (
        select(Book)
        .where(Book.library_id == library_id)
        .order_by(Book.title.asc())
    )

    return list(db.scalars(statement).all())

def get_book(
    db: Session,
    library_id: int,
    book_id: int,
) -> Book | None:
    statement = (
        select(Book)
        .where(
            Book.id == book_id,
            Book.library_id == library_id,
        )
    )

    return db.scalar(statement)

def create_book(
    db: Session,
    data,
) -> Book:
    book = Book(
        library_id=data.library_id,
        book_code=data.book_code,
        title=data.title,
        author=data.author,
        publisher=data.publisher,
        category=data.category,
        isbn=data.isbn,
        total_copies=data.total_copies,
        available_copies=data.total_copies,
    )

    db.add(book)
    db.commit()
    db.refresh(book)

    return 

def update_book(
    db: Session,
    book: Book,
    data,
) -> Book:
    update_data = data.model_dump(
        exclude_unset=True
    )

    if "total_copies" in update_data:
        new_total = update_data["total_copies"]

        currently_issued = (
            book.total_copies - book.available_copies
        )

        if new_total < currently_issued:
            raise ValueError(
                "Total copies cannot be less than "
                "the number of currently issued copies."
            )

        book.available_copies = (
            new_total - currently_issued
        )

    for field, value in update_data.items():
        if field != "total_copies":
            setattr(book, field, value)

    db.commit()
    db.refresh(book)

    return book

def delete_book(
    db: Session,
    book: Book,
) -> None:
    active_transaction = db.scalar(
        select(BookTransaction).where(
            BookTransaction.book_id == book.id
        )
    )

    if active_transaction:
        raise ValueError(
            "Book cannot be deleted because "
            "it is currently issued."
        )

    db.delete(book)
    db.commit()

