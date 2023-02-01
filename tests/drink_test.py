import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Americano", 2.00, 6)
    
    def test_has_name(self):
        self.assertEqual("Americano", self.drink.name)

    def test_has_price(self):
        self.assertEqual(2.00, self.drink.price)

    def test_has_caffeine_level(self):
        self.assertEqual(6, self.drink.caffeine_level)