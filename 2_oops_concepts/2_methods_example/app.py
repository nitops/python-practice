""" to demonstrate class methods vs regular method"""


class Employee:
    raise_amount = 1.04  # defining class variable raise_pay as 4%
    num_of_employees = 0  # another class variable

    #  regular method since its takes self as first argument
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name + '.' + last_name + '@mycompany.com'
        self.pay = pay

        Employee.num_of_employees += 1  # note that for num_of_employees we have not used self because we don't want
        # total number of employees to be different for any one instance

    #  class method since its takes self as first argument




emp1 = Employee("suman", "jain", 50000)  # emp1 is an instance of Employee class
emp2 = Employee("rakesh", "kumar", 70000)  # emp2 is an instance of Employee class
emp3 = Employee("rashmi", "sinha", 60000)  # emp3 is an instance of Employee class
emp4 = Employee("rahul", "bansal", 40000)  # emp3 is an instance of Employee class

print(Employee.num_of_employees)  # it prints 4 , since there are 4 times __init__ is called
