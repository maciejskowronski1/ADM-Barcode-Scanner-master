from Db.DbDecorators import update, query
from typing import Any, Union, List, Tuple

from Model.Barcode import Barcode


@update('barcode.db')
def create_table(table: str, *args: str) -> Tuple[str, Tuple]:
    columns = ', '.join(args)
    sql = f'''
        CREATE TABLE IF NOT EXISTS {table} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            {columns}
        )
    '''
    values = ()
    return sql, values


@update('barcode.db')
def insert(table: str, barcode: Barcode) -> Tuple[str, Tuple[Any, ...]]:
    columns = 'code, name, price'
    values = (barcode.code, barcode.name, barcode.price)
    sql = f'insert into {table} ({columns}) values (?, ?, ?)'
    return sql, values


@update('barcode.db')
def insert_multiple(table: str, barcodes: List[Barcode]) -> Tuple[str, List[Tuple[Any, ...]]]:
    columns = 'code, name, price'
    values = [(b.code, b.name, b.price) for b in barcodes]
    flattened_values = [val for sublist in values for val in sublist]
    placeholders = ','.join(['?' for _ in range(len(columns.split(',')))])
    placeholders = ','.join([f'({placeholders})' for _ in range(len(barcodes))])
    sql = f'insert into {table} ({columns}) values {placeholders}'
    return sql, flattened_values


@update('barcode.db')
def update(table: str, barcode: Barcode) -> Tuple[str, Tuple[Any, ...]]:
    columns = 'code = ?, name = ?, price = ?'
    values = (barcode.code, barcode.name, barcode.price)
    sql = f'update {table} set {columns} where id = {barcode.id}'
    return sql, values


@query('barcode.db')
def get_all(table: str) -> str:
    sql = f'select * from {table}'
    return sql


@query('barcode.db')
def get_one(table: str, search_criteria: tuple):
    column, value = search_criteria
    sql = f"SELECT * FROM {table} WHERE {column} = '{value}'"
    return sql
