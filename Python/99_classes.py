# Classes

class Employee:
    
    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        self.email = firstName + '.' + lastName + '@company.com'

    def fullname(self):
        return f"{self.firstName} {self.lastName}"     #  w/o the f-string >> return '{} {}'.format(self.firstName, self.lastName)

emp_1 = Employee ('Athemax', 'Rayton', 50_000)
emp_2 = Employee ('Antithemax', 'Raynogolon', 65_000)


print(emp_1.fullname()) # This is a method & requires ()
print(emp_2.fullname()) # This is a method & requires ()