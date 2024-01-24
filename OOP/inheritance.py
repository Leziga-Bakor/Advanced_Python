class Employee:
    raise_amt = 1.04
    def __init__(self, firstname, lastname, pay):
        self.first = firstname
        self.last = lastname
        self.email = firstname.lower() + '.' + lastname.lower() + '@email.com'
        self.pay = pay

    def fullname(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, firstname, lastname, pay, prog_lang):
        super().__init__(firstname, lastname, pay)
        # Employee.__init__(self, firstname, lastname, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, firstname, lastname, pay, employees=None):
        super().__init__(firstname, lastname, pay)
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

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer('John', 'Doe', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'C++')

print(dev_1.email)
print(dev_1.prog_lang)
print(dev_1.fullname())
print(dev_2.pay)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

mgr_1 = Manager('Erik', 'Ten_Hag', 100000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.print_emp()

mgr_1.remove_emp(dev_1)
mgr_1.print_emp()

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

print(issubclass(Manager, Employee))
print(issubclass(Employee, Developer))