from sqlalchemy import inspect

from app.database.session import engine


inspector = inspect(engine)

for table in inspector.get_table_names():
    print(f"\n{'=' * 50}")
    print(f"TABLE: {table}")
    print(f"{'=' * 50}")

    for column in inspector.get_columns(table):
        print(
            f"Column:   {column['name']}\n"
            f"Type:     {column['type']}\n"
            f"Nullable: {column['nullable']}\n"
            f"Default:  {column['default']}\n"
        )