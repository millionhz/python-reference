class Item:

    pay_rate = 0.8

    def __init__(self, name: str, price: int, quantity=0) -> None:
        assert price >= 0, "Price must be a positive number"
        assert quantity >= 0, "Quantity must be a positive number"

        self.__name = name
        self.__price = price
        self.quantity = quantity

    # https://stackoverflow.com/questions/6930144/underscore-vs-double-underscore-with-variables-and-methods
    # public
    # _protected
    # __private
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 10:
            self.__name = name

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price *= self.pay_rate

    def apply_increment(self, increment_amount):
        self.__price += self.price*increment_amount

    def calculate_price(self) -> int:
        return self.__price * self.quantity

    @classmethod
    def instantiate_objects(cls, data: list) -> list:
        objects = []

        for values in data:
            objects.append(Item(*values))

        return objects

    @staticmethod
    def is_integer(val) -> bool:
        return isinstance(val, int)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
