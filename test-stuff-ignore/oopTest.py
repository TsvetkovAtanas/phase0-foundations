

from car import Car
from truck import Truck


car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue",  True)

print(car1.model)

car1.drive()
car1.stop()

car2.describe()

print(Car.year_delivered)
print(f"There are currently {Car.number_of_cars} cars.")

truck1 = Truck("Scania", 2026, "yellow", True)

truck1.describe()