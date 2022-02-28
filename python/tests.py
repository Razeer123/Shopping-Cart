import unittest

from python.pricer import Pricer
from shopping_cart import ShoppingCartConcreteCreator, Order
from test_utils import Capturing


class ShoppingCartTest(unittest.TestCase):

    def test_print_header(self):
        sc = ShoppingCartConcreteCreator().operation()
        with Capturing() as output:
            sc.print_receipt()
        self.assertEqual("------------RECEIPT------------", output[0].replace(" ", ""))

    def test_print_names_default_order(self):
        sc = ShoppingCartConcreteCreator().operation()
        with Capturing() as output:
            sc.print_receipt()
        self.assertEqual("NameQuantityPrice", output[1].replace(" ", ""))

    def test_print_names_custom_order(self):
        sc = ShoppingCartConcreteCreator().operation([Order.NAME, Order.PRICE, Order.QUANTITY])
        with Capturing() as output:
            sc.print_receipt()
        self.assertEqual("NamePriceQuantity", output[1].replace(" ", ""))

    def test_print_names_wrong_arguments(self):
        sc = ShoppingCartConcreteCreator().operation([Order.NAME, 4, 'WrongArgument'])
        with Capturing() as output:
            sc.print_receipt()
        self.assertEqual("NameQuantityPrice", output[1].replace(" ", ""))

    def test_print_receipt(self):
        sc = ShoppingCartConcreteCreator().operation()
        pricer = Pricer()
        database = pricer.get_database()
        items = {}
        count = 2
        total_price = 0
        for item in database:
            price = pricer.get_price(item) / 100
            items[item] = price
            total_price += price * count
            sc.add_item(item, count)
        with Capturing() as output:
            sc.print_receipt()
        for index, item in enumerate(items):
            self.assertEqual(f'{item}{count}€{items.get(item)}', output[index + 2].replace(" ", ""))
        self.assertEqual(f'Total:€{total_price:.2f}', output[len(output) - 1].replace(" ", ""))

    def test_doesnt_explode_on_mystery_item(self):
        sc = ShoppingCartConcreteCreator().operation()
        pricer = Pricer()
        database = pricer.get_database()
        items = {}
        count = 2
        for item in database:
            items[item] = pricer.get_price(item) / 100
            sc.add_item(item, count)
        sc.add_item("pear", 5)
        with Capturing() as output:
            sc.print_receipt()
        for index, item in enumerate(items):
            self.assertEqual(f'{item}{count}€{items.get(item)}', output[index + 2].replace(" ", ""))


unittest.main(exit=False)
