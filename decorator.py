from abc import ABC, abstractmethod

class SimpleCoffee:
    def cost(self):
        return 5

class MilkDecorator:
    def __init__(self, beverage):
        self.beverage = beverage

    def cost(self):
        return self.beverage.cost() + 2

class SugarDecorator:
    def __init__(self, beverage):
        self.beverage = beverage

    def cost(self):
        return self.beverage.cost() + 1


coffee = SimpleCoffee()
print("Base Coffee:", coffee.cost())  

coffee_with_milk = MilkDecorator(coffee)
print("Coffee with milk:", coffee_with_milk.cost())  

coffee_with_milk_sugar = SugarDecorator(coffee_with_milk)
print("Coffee with milk and sugar:", coffee_with_milk_sugar.cost()) 