"""A class that can be used to represent a car."""


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, _make:str, _model:str, _year:int) -> None:
        self.make:str = _make
        self.model:str = _model
        self.year:int =  _year
        self.odometer_reading:int = 0

    
    def get_descriptive_name(self)->str:
        long_name:str = f'{self.year} {self.make} {self.model}'
        return long_name
    
    def read_odometer(self)->int:
        print(f"This car has {self.odometer_reading} miles on it.")
    

    def update_odometer(self, mileage)->None:
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading =mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles:int)->None:
        self.odometer_reading+= miles



