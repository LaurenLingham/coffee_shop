import unittest
from src.customer import Customer
from src.coffee_shop import CoffeeShop
from src.drink import Drink
from src.food import Food

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Larry King", 50.00, 87, 5)

    def test_has_name(self):
        self.assertEqual("Larry King", self.customer.name)
    
    def test_has_wallet(self):
        self.assertEqual(50.00, self.customer.wallet)

    def test_has_energy_level(self):
        self.assertEqual(5, self.customer.energy_level)

    def test_can_buy_drink(self):
        drink = Drink("Americano", 2.00, 6)
        self.customer.buy_drink(drink)
        self.assertEqual(48.00, self.customer.wallet)
        self.assertEqual(11, self.customer.energy_level)

    def can_buy_food(self):
        food = Food("Burger", 5.00, 3)
        self.customer.buy_food(food)
        self.assertEqual(45.00, self.customer.wallet)
        self.assertEqual(2, self.customer.energy_level)