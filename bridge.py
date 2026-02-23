from abc import ABC, abstractmethod

class Packager(ABC):
    @abstractmethod
    def pack(self, content):
        pass

class CupPackager(Packager):
    def pack(self, content):
        return f"{content} served in a cup"

class BottlePackager(Packager):
    def pack(self, content):
        return f"{content} served in a bottle"

class BeverageWithPack:
    def __init__(self, name, packager: Packager):
        self.name = name
        self.packager = packager

    def serve(self):
        print(self.packager.pack(self.name))


coffee_in_cup = BeverageWithPack("Coffee", CupPackager())
tea_in_bottle = BeverageWithPack("Tea", BottlePackager())

coffee_in_cup.serve()  
tea_in_bottle.serve()  