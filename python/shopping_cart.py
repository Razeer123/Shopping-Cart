from abc import ABC, abstractmethod
from typing import OrderedDict
from enum import Enum

from shopping_cart_interface import IShoppingCart
from pricer import Pricer


class Order(Enum):
    NAME = 1
    PRICE = 2
    QUANTITY = 3


class ShoppingCart(IShoppingCart):
    """
    Implementation of the shopping tills in our supermarket.
    """

    def __init__(self, pricer: Pricer, order: list):
        self.pricer = pricer
        self._contents: OrderedDict[str, int] = OrderedDict[str, int]()
        self._order: list = order
        database = self.pricer.get_database()
        if len(database) > 0:
            self.max_width = max(len(x) for x in self.pricer.get_database()) + 10
        else:
            self.max_width = 10

    def add_item(self, item_type: str, number: int):
        # adds new item to or update existing item in the shopping cart
        if item_type not in self._contents:
            self._contents[item_type] = number
        else:
            self._contents[item_type] = self._contents[item_type] + number

    def print_receipt(self):
        total_price = 0
        default_order = ['Name', 'Quantity', 'Price']
        input_order = []
        for item in self._order:
            if item == Order.PRICE:
                input_order.append("Price")
            elif item == Order.NAME:
                input_order.append("Name")
            elif item == Order.QUANTITY:
                input_order.append("Quantity")
            else:
                input_order = default_order
                break
        print('------------ RECEIPT ------------')
        print(f'{input_order[0]: <{self.max_width}} {input_order[1]: <{self.max_width}} {input_order[2]: <{self.max_width}}')
        for key, value in self._contents.items():
            price = self.pricer.get_price(key) / 100
            total_price += price * value
            values = {"Name": key, "Quantity": value, "Price": "€" + str(price)}
            print(f"{values.get(input_order[0]): <{self.max_width}} {values.get(input_order[1]): <{self.max_width}} {values.get(input_order[2]): <{self.max_width}}")
        print(f'Total: €{total_price:.2f}')


class ShoppingCartCreator(ABC):
    """
    Interface for the ShoppingCart creator.
    The creation process will be delegated to the subclasses of this class.
    """

    @abstractmethod
    def factory_method(self, order) -> ShoppingCart:
        # return the ShoppingCart object
        pass

    def operation(self, order=None) -> ShoppingCart:
        # Here more operations can be performed on the ShoppingCart object
        # returns ShoppingCart object
        return self.factory_method(order)


class ShoppingCartConcreteCreator(ShoppingCartCreator):
    """
    Concrete class for the ShoppingCart creator.
    Implements the factory_method
    """

    def factory_method(self, order) -> ShoppingCart:
        # returns ShoppingCart object
        if type(order) is list and len(order) == 3:
            return ShoppingCart(Pricer(), order)
        return ShoppingCart(Pricer(), [Order.NAME, Order.QUANTITY, Order.PRICE])
