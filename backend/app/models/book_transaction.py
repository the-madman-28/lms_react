from datetime import date, datetime

from sqlalchemy import Date, DateTime, ForeignKey, Integer, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class BookTransaction(Base):
    __tablename__ = "book_transactions"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    library_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("libraries.id"),
        nullable=False,
    )

    history_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("transaction_history.id"),
        nullable=False,
    )

    book_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("books.id"),
        nullable=False,
    )

    employee_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("employees.id"),
        nullable=False,
    )

    issue_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    due_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    remarks: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.current_timestamp(),
    )