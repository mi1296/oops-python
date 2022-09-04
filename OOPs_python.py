"""
Python OOPs Tutorial by Corey Schafer
https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc
"""


class Employee:

    no_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.no_of_emps += 1

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_str(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def isworkday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->'+emp.fullname())



#Employee.set_raise_amt(1.05)
#print(Employee.no_of_emps)
emp_1 = Employee('Test', 'User', 50000)
#print(Employee.no_of_emps)
emp_2 = Employee('Frankie', 'Bergstein', 5000000)
#print(Employee.no_of_emps)
emp_3 = Employee('Grace', 'Hanson', 5000000)


#print(emp_1.email)
#print(emp_2.last)
#print(emp_1.fullname())
#print(emp_1.fullname())
#print(Employee.fullname(emp_1))

#print(emp_1.pay)
#emp_1.apply_raise()
#print(emp_1.pay)

#print(emp_1.__dict__)

#emp_1.raise_amount = 1.05
#print(Employee.raise_amount)
#print(emp_1.raise_amount)
#print(emp_2.raise_amount)

#print(emp_1.__dict__)

#print(Employee.no_of_emps)

#print(Employee.raise_amount)
#print(emp_1.raise_amount)
#print(emp_2.raise_amount)
#print(emp_3.raise_amount)

#emp_4_string = 'John-Doe-70000'
#emp_5_string = 'Steve-Smith-80000'
#emp_6_string = 'John-Adams-90000'

#emp_4 = Employee.from_str(emp_4_string)
#print(emp_4.email)
#print(emp_4.first)
#print(emp_4.last)
#print(emp_4.pay)

"""
import datetime
my_date = datetime.date(2022, 10, 16)
print(Employee.isworkday(my_date))
"""

dev_1 = Developer('Sol', 'Bergstein', 60000, 'Python')
dev_2 = Developer('Robert', 'Hanson', 68000, 'Java')
#print(dev_1.email)
#print(dev_1.prog_lang)

#print(help(Developer))

mgr_1 = Manager('Sue', 'Smith', 900000, [dev_1])
#mgr_1.print_emps()
mgr_1.add_emp(dev_2)
#mgr_1.print_emps()
mgr_1.remove_emp(dev_1)
#mgr_1.print_emps()

#print(isinstance(mgr_1, Manager))
#print(issubclass(Manager, Employee))

#print(emp_1)

#print(emp_1.__repr__())
#print(emp_1.__str__())
#print(emp_1+emp_2)
#print(len(emp_1))

print(emp_1.email)
print(emp_1.fullname)
emp_1.fullname = 'Mallory Smith'
print(emp_1.email)
print(emp_1.fullname)