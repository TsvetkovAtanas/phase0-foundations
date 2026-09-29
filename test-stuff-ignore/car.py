class Car:

    year_delivered = 2023
    number_of_cars = 0

    # Constructor - needed in order to create objects
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        Car.number_of_cars += 1

    def drive(self):
        print(f"Dringing the {self.model}...")

    def stop(self):
        print(f"Stoppping the {self.model}...") 

    def describe(self):
        print(f"This car is {self.model}, {self.year}, {self.color}")
