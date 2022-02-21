class Employee:
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name + '.' + last_name + '@mycompany.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)


emp1 = Employee("suman", "jain", 50000)  # emp1 is an instance of Employee class
emp2 = Employee("rakesh", "kumar", 70000)  # emp2 is an instance of Employee class

# printing emails of employee
print(emp1.email)
print(emp2.email)

# print full name of employee
print(
    emp1.fullname())  # here we are calling method via instance of class so it will pass instance name as 'self' automatically

# print full name via class directly
print(Employee.fullname(
    emp1))  # here we are calling method via class name so instance of class need to be explictly passed
# as it doesn't know which instance to run with the given method.

""" infact in the background emp1.fullname() is transformed into Employee.fullname(emp1) when method is invoked"""
