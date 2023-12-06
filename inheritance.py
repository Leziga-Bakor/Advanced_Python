class Employee:
    raise_amt = 1.04
    def __init__(self, firstname, lastname, pay):
        self.first = firstname
        self.last = lastname
        self.email = firstname.lower() + '.' + lastname.lower() + '@gmail.com'
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




dev_1 = Developer('John', 'Doe', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'C++')

print(dev_1.email)
print(dev_1.prog_lang)
print(dev_1.fullname())
print(dev_2.pay)


print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
