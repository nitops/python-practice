"""  extending Employee class from previous example"""


class Employee:
    raise_amount = 1.04  # defining class variable raise_pay as 4%
    num_of_employees = 0

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name + '.' + last_name + '@mycompany.com'
        self.pay = pay

        Employee.num_of_employees += 1  # note that for num_of_employees we have not used self because we don't want
        # total number of employees to be different for any one instance


    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp1 = Employee("suman", "jain", 50000)  # emp1 is an instance of Employee class
emp2 = Employee("rakesh", "kumar", 70000)  # emp2 is an instance of Employee class
emp3 = Employee("rashmi", "sinha", 60000)  # emp3 is an instance of Employee class
emp4 = Employee("rahul", "bansal", 40000)  # emp3 is an instance of Employee class

print(Employee.num_of_employees)  # it prints 4 , since there are 4 times __init__ is called

""" case1: changing emp1 data via emp1 instance """
print(emp1.pay)  # print original pay
emp1.apply_raise()  # apply raise
print(emp1.pay)  # print new pay - data of instance emp1 class is changed

""" case2: changing emp2 data via class directly"""
print(emp2.pay)  # print original pay
Employee.apply_raise(emp2)
print(emp2.pay)  # print new pay

""" changing class variable value via class instance and verifying results"""

emp3.raise_amount = 1.05  # changing raise amt just for emp3

print(Employee.raise_amount)

print(emp3.pay)
Employee.apply_raise(emp3)
print(emp3.pay)  # note that here raise of 5% is applied for emp3 but not 4%

''' output: 
4
50000
52000
70000
72800
1_first_class_fucntions.04
60000
63000
'''