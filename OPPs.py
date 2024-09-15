# OOPS Concepts: Classes, Objects, Inheritance, Polymorphism, Encapsulation, Abstraction
#Classes: Employee, Manager, AbstractEmployee, and ConcreteEmployee are classes.
#Objects: emp, mgr, and abs_emp are objects created from classes.
#Inheritance: Manager inherits from Employee.
#Polymorphism: calculate_bonus method is overridden in Manager class.
#Encapsulation: Employee details are hidden using private attributes (__name, __age, __salary).
#Abstraction: AbstractEmployee is an abstract class with an abstract method calculate_tax. ConcreteEmployee is a concrete class implementing the abstract class.

# Class: Employee
class Employee:
    # Constructor
    def __init__(self, name, age, salary):
        # Encapsulation: Hiding data
        self.__name = name
        self.__age = age
        self.__salary = salary

    # Method: Display employee details
    def display_details(self):
        print(f"Name: {self.__name}, Age: {self.__age}, Salary: {self.__salary}")

    # Method: Calculate bonus
    def calculate_bonus(self):
        return self.__salary * 0.1

# Inheritance: Manager inherits from Employee
class Manager(Employee):
    # Constructor
    def __init__(self, name, age, salary, team_size):
        super().__init__(name, age, salary)
        self.__team_size = team_size

    # Method: Display manager details
    def display_details(self):
        super().display_details()
        print(f"Team Size: {self.__team_size}")

    # Polymorphism: Overriding calculate_bonus method
    def calculate_bonus(self):
        return super().calculate_bonus() + (self.__team_size * 1000)

# Abstraction: Abstract class with abstract method
from abc import ABC, abstractmethod

class AbstractEmployee(ABC):
    @abstractmethod
    def calculate_tax(self):
        pass

# Concrete class implementing abstract class
class ConcreteEmployee(AbstractEmployee):
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def calculate_tax(self):
        return self.__salary * 0.2

# Creating objects
emp = Employee("John", 30, 50000)
mgr = Manager("Jane", 35, 80000, 10)
abs_emp = ConcreteEmployee("Bob", 25, 40000)

# Displaying details
emp.display_details()
mgr.display_details()
abs_emp.calculate_tax()

# Calculating bonus
print(f"Employee Bonus: {emp.calculate_bonus()}")
print(f"Manager Bonus: {mgr.calculate_bonus()}")

# Calculating tax
print(f"Concrete Employee Tax: {abs_emp.calculate_tax()}")