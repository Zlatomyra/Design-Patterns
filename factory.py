from abc import ABC, abstractmethod

class Beverage(ABC):
    @abstractmethod
    def prepare(self):
        pass

class Coffee(Beverage):
    def prepare(self):
        return "Preparing Coffee"

class Tea(Beverage):
    def prepare(self):
        return "Preparing Tea"

class BeverageCreator(ABC):
    @abstractmethod
    def create_beverage(self) -> Beverage:
        pass

class CoffeeCreator(BeverageCreator):
    def create_beverage(self) -> Beverage:
        return Coffee()

class TeaCreator(BeverageCreator):
    def create_beverage(self) -> Beverage:
        return Tea()

def order_beverage(creator: BeverageCreator):
    beverage = creator.create_beverage()
    print(beverage.prepare())

order_beverage(CoffeeCreator()) 
order_beverage(TeaCreator())    