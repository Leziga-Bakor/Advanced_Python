class Person():

    def __init__(self, name, age, gender):

        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, value):
        if isinstance(str, value):
            self.__name = value
        else:
            return 'Name must be of type string'
        
p1 = Person('Joe', 30, 'm')
print(p1.Name)

