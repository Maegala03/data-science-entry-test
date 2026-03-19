# Q7: Car Class Implementation

class Car:
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """
    
    def __init__(self, make, model, year):
        """Initialize the car with make, model, and year attributes"""
        self.make = make
        self.model = model
        self.year = year
    
    def describe_car(self):
        """Print car information in format: Year Make Model"""
        print(f"{self.year} {self.make} {self.model}")

# Basic test
my_car = Car("Toyota", "Camry", 2020)
my_car.describe_car()

another_car = Car("Honda", "Civic", 2019)
another_car.describe_car()

Answer:

2020 Toyota Camry
2019 Honda Civic

Explanation:

Class Components:
__init__ method: Constructor that initializes the car object
self.make: Stores the car's make (e.g., "Toyota")
self.model: Stores the car's model (e.g., "Camry")
self.year: Stores the car's year (e.g., 2020)
Method:
describe_car(): Prints car info in "Year Make Model" format
Uses f-string: f"{self.year} {self.make} {self.model}"
Object Creation:
Car("Toyota", "Camry", 2020): Creates car object with specified attributes
my_car.describe_car(): Calls method to print car information


# Q7 Task 2: Create Car instance with specified attributes

class Car:
    """
    Define a class named Car with attributes: make, model, year
    Initialize these attributes in the __init__ method
    Add a method named describe_car() that prints information about the car as "Year Make Model"
    """
    
    def __init__(self, make, model, year):
        """Initialize the car with make, model, and year attributes"""
        self.make = make
        self.model = model
        self.year = year
    
    def describe_car(self):
        """Print car information in format: Year Make Model"""
        print(f"{self.year} {self.make} {self.model}")

# Task 2: Create instance with specified attributes
# Make: Toyota, Model: Corolla, Year: 2020
toyota_corolla = Car("Toyota", "Corolla", 2020)
toyota_corolla.describe_car()

Answer: 

2020 Toyota Corolla


Explanation:

Object Creation: Car(...) makes a new car with specific attributes.
Variable Storage: toyota_corolla holds reference to the car object.
Method Call: toyota_corolla.describe_car() tells that specific car to describe itself.
Self Reference: Inside the method, self refers to toyota_corolla.


