import unittest
from src.coffee_shop import CoffeeShop
from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestCoffeeShop(unittest.TestCase):
    def setUp(self):
        self.coffee_shop = CoffeeShop("The Prancing Pony", 100.00)

    def test_has_name(self):
        self.assertEqual("The Prancing Pony", self.coffee_shop.name)

    def test_has_till(self):
        self.assertEqual(100.00, self.coffee_shop.till)

    def test_increase_till(self):
        self.coffee_shop.increase_till(10.00)
        self.assertEqual(110.00, self.coffee_shop.till)

    def test_sell_drink__true(self):
        customer = Customer("Larry King", 50.00, 87, 5)
        drink = Drink("Americano", 2.00, 6)
        self.coffee_shop.sell_drink(drink, customer)
        self.assertEqual(102.00, self.coffee_shop.till)
        self.assertEqual(48.00, customer.wallet)

    def test_sell_drink__false(self):
        customer = Customer("Larry King", 50.00, 87, 5)
        drink = Drink("Potato", 2.00, 6)
        self.coffee_shop.sell_drink(drink, customer)
        self.assertEqual(100.00, self.coffee_shop.till)
        self.assertEqual(50.00, customer.wallet)

    def test_sell_drink_overage__true(self):
        customer = Customer("Larry King", 50.00, 87, 5)
        drink = Drink("Americano", 2.00, 6)
        self.coffee_shop.sell_drink_with_checks(drink, customer)
        self.assertEqual(102.00, self.coffee_shop.till)
        self.assertEqual(48.00, customer.wallet)
       
    def test_sell_drink_overage__false(self):
        customer = Customer("Tinky Winky", 10.00, 12, 3)
        drink = Drink("Americano", 2.00, 6)
        fail_test = self.coffee_shop.sell_drink_with_checks(drink, customer)
        self.assertEqual(100.00, self.coffee_shop.till)
        self.assertEqual(10.00, customer.wallet)
        self.assertEqual(fail_test, None)

    def test_caffeine_level__fail(self):
        customer = Customer("Larry King", 50.00, 87, 11)
        drink = Drink("Americano", 2.00, 6)
        fail_test = self.coffee_shop.sell_drink_with_checks(drink, customer)
        self.assertEqual(fail_test, None)

    def test_check_stock_values(self):
        self.assertEqual(100, self.coffee_shop.stock_value())

