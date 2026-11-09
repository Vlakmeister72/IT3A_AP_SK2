import random
from datetime import datetime

class Car:
    def __init__(self, brand:str, model:str, year:int, ins_year:int, fuel:int = 100):
        self.brand = brand
        self.model = model
        self.year = year
        self.ins_year = ins_year
        self.fuel = fuel
        pass

    def __str__(self): #metoday, která se volá jako základní pro výpis vlastností
        return f"{self.brand} {self.model} ({self.year}) - fuel: {self.fuel} %"
    
    def move(self):
        usage = random.randint(20, 30)
        if self.fuel >= usage:
            self.fuel -= usage
            return f"{self.brand} {self.model} has used up {usage} % of fuel and {self.fuel} % remains."
        else:
            return f"{self.brand} {self.model} wouldn't make it to the destination. It needs {usage} % of fuel and only has {self.fuel} %"
        
    def full_fill(self):
        filled = 100 - self.fuel
        self.fuel = 100
        return f"{self.brand} {self.model} filled up with {filled} % of fuel."
    
    def inspection(self):
        if self.ins_year < datetime.now().year:
            return f"{self.brand} {self.model} needs to undergo an inspection. The registration date has expired in {self.ins_year}."
        else:
            return f"{self.brand} {self.model} has their registration up to date, no need to go into inspection until {self.ins_year}."

    
car1 = Car("Ferrari", "458 Italia", 2009, 2019, 100)
car2 = Car("Lamborghini", "Huracán", 2014, 2028, 77)
car3 = Car("Bugatti", "Veyron", 2005, 2025, 67)

#testovací výpis
print(car1)
print(car2)
print(car3)

#testovací jízda
print(car1.move())
print(car2.move())
print(car3.move())

#tankování
print(car3.full_fill())

#STK
print(car1.inspection())
print(car2.inspection())
print(car3.inspection())

class Garage:
    def __init__(self, name:str):
        self.name = name
        self.cars = []
        pass
    
    def add_car(self, car:Car):
        self.cars.append(car)
        return f"{car.brand} {car.model} was added to garage {self.name}."
    
garage = Garage("Underground garage")

print(garage.add_car(car1))
print(garage.add_car(car2))
print(garage.add_car(car3))

