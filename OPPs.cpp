#include <iostream>
#include <string>

// OOPS Concepts: Classes, Objects, Inheritance, Polymorphism, Encapsulation, Abstraction

// Class: Employee
class Employee {
private:
    std::string name;
    int age;
    double salary;

public:
    // Constructor
    Employee(std::string name, int age, double salary) 
        : name(name), age(age), salary(salary) {}

    // Method: Display employee details
    void displayDetails() const {
        std::cout << "Name: " << name << ", Age: " << age << ", Salary: " << salary << std::endl;
    }

    // Method: Calculate bonus
    double calculateBonus() const {
        return salary * 0.1;
    }

    // Getter methods for encapsulated data
    std::string getName() const { return name; }
    int getAge() const { return age; }
    double getSalary() const { return salary; }
};

// Inheritance: Manager inherits from Employee
class Manager : public Employee {
private:
    int teamSize;

public:
    // Constructor
    Manager(std::string name, int age, double salary, int teamSize) 
        : Employee(name, age, salary), teamSize(teamSize) {}

    // Method: Display manager details
    void displayDetails() const {
        Employee::displayDetails();
        std::cout << "Team Size: " << teamSize << std::endl;
    }

    // Polymorphism: Overriding calculateBonus method
    double calculateBonus() const {
        return Employee::calculateBonus() + (teamSize * 1000);
    }
};

// Abstraction: Abstract class with abstract method
class AbstractEmployee {
public:
    virtual ~AbstractEmployee() {}
    virtual double calculateTax() const = 0;
};

// Concrete class implementing abstract class
class ConcreteEmployee : public AbstractEmployee {
private:
    std::string name;
    int age;
    double salary;

public:
    // Constructor
    ConcreteEmployee(std::string name, int age, double salary) 
        : name(name), age(age), salary(salary) {}

    // Method: Calculate tax
    double calculateTax() const override {
        return salary * 0.2;
    }
};

int main() {
    // Creating objects
    Employee emp("John", 30, 50000.0);
    Manager mgr("Jane", 35, 80000.0, 10);
    ConcreteEmployee absEmp("Bob", 25, 40000.0);

    // Displaying details
    emp.displayDetails();
    mgr.displayDetails();
    std::cout << "Concrete Employee Tax: " << absEmp.calculateTax() << std::endl;

    // Calculating bonus
    std::cout << "Employee Bonus: " << emp.calculateBonus() << std::endl;
    std::cout << "Manager Bonus: " << mgr.calculateBonus() << std::endl;

    return 0;
}