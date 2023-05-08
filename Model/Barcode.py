class Barcode:
    def __init__(self, code, name, price, id_code=None):
        self.id = id_code
        self.code = code
        self.name = name
        self.price = price

    @classmethod
    def from_cursor(cls, cursor):
        id_code, code, name, price = cursor
        return cls(id_code=id_code, code=code, name=name, price=price)

    @classmethod
    def without_id(cls, code, name, price):
        return cls(code=code, name=name, price=price)

    def set_price(self, price:float):
        self.price = price

    def __str__(self):
        return f'''Product id:{self.id}, code:{self.code}, name:{self.name}, price{self.price} '''