from sqlalchemy import inspect

from app.database.session import engine
from app.models import (
    Book,
    BookTransaction,
    Employee,
    Library,
    TransactionHistory,
    User,
)


models = [
    Library,
    User,
    Book,
    Employee,
    TransactionHistory,
    BookTransaction,
]

inspector = inspect(engine)

all_ok = True

for model in models:
    table_name = model.__tablename__

    db_columns = {
        column["name"]
        for column in inspector.get_columns(table_name)
    }

    model_columns = {
        column.name
        for column in model.__table__.columns
    }

    missing_in_model = db_columns - model_columns
    extra_in_model = model_columns - db_columns

    print(f"\n{'=' * 60}")
    print(f"TABLE: {table_name}")
    print(f"{'=' * 60}")

    if not missing_in_model and not extra_in_model:
        print("✓ Columns match")
    else:
        all_ok = False

        if missing_in_model:
            print("Missing in model:", missing_in_model)

        if extra_in_model:
            print("Extra in model:", extra_in_model)


print("\n" + "=" * 60)

if all_ok:
    print("✓ ALL MODELS MATCH THE DATABASE")
else:
    print("✗ MODEL/DATABASE MISMATCH FOUND")