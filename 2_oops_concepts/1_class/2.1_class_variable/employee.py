"""  extending Employee class from previous example"""


class Employee:
    raise_amount = 1.04  # defining class variable raise_pay as 4%
    num_of_employees = 0 # another class variable

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

# check what values are contained in instance variable, note that it will not print raise_amount as its class varialbe.
print(emp1.__dict__)

# now checking for Employee class,
print(Employee.__dict__)