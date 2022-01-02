from item import Item


class Phone(Item):

    def __init__(self, name: str, price: int, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)

        assert broken_phones >= 0, "Broken Phones must be a positive number"

        self.broken_phones = broken_phones

    def __repr__(self) -> str:
        return super().__repr__() + "\b" + f", {self.broken_phones})"
