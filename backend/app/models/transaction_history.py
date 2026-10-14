from datetime import date, datetime

from sqlalchemy import Date, DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class TransactionHistory(Base):
    __tablename__ = "transaction_history"

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

    book_code: Mapped[str] = mapped_column(
        String(80),
        nullable=False,
    )

    book_title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    employee_code: Mapped[str] = mapped_column(
        String(80),
        nullable=False,
    )

    employee_name: Mapped[str] = mapped_column(
        String(255),
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

    return_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        server_default="ISSUED",
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