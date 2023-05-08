import sqlite3
from typing import Callable

from Model.Barcode import Barcode


def update(db_name: str):
    def decorator(fun: Callable[..., str]):
        def wrapper(*args, **kwargs):
            with sqlite3.connect(db_name) as connection:
                cursor = connection.cursor()
                try:
                    sql, values = fun(*args, **kwargs)
                    print(sql, values)
                    cursor.execute(sql, values)
                except sqlite3.Error as e:
                    print(f"An error occurred: {e}")
                    connection.rollback()
                    return None
                else:
                    connection.commit()
                    return cursor

        return wrapper

    return decorator


def query(db_name: str):
    def decorator(fun):
        def wrapper(*args, **kwargs):
            with sqlite3.connect(db_name) as connection:
                try:
                    sql = fun(*args, **kwargs)
                    print(sql)
                    cursor = connection.cursor()
                    cursor.execute(sql)
                    records = cursor.fetchall()
                    return [Barcode.from_cursor(c) for c in records]
                except sqlite3.Error as e:
                    print(f"SQLite error: {e}")
                    return []

        return wrapper

    return decorator
