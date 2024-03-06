class Language:
    def say_hello(self):
        raise NotImplementedError('Please use say_hello method in child class')
    
class French(Language):
    def say_hello(self):
        print('Bonjour')

class Chinese(Language):
    def say_hello(self):
        print('Ni hou')

def intro(lang):
    lang.say_hello()

sarthak = French()
john = Chinese()

intro(sarthak)
intro(john)
