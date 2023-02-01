class CoffeeShop:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = {
            "Mocha": [10, 1], 
            "Americano": [20, 1], 
            "Hot Chocolate": [30, 1],
            "Tea": [40, 1]
        }

    def increase_till(self, amount):
        self.till += amount

    def sell_drink(self, drink, customer):
        for item in self.drinks:
            if item == drink.name:
                self.increase_till(drink.price)
                customer.buy_drink(drink)
        return None

    def age_check(self, customer):
        return customer.age >= 16

    def energy_check(self, customer):
        return customer.energy_level <=10

    def sell_drink_with_checks(self, drink, customer):
        if self.age_check(customer) and self.energy_check(customer):
            self.sell_drink(drink, customer)

    def stock_value(self):
        total = 0
        for item in self.drinks.values():
            total += item[0] * item[1]
        return total