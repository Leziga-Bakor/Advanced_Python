class French:
    def say_hello(self):
        print('Bonjour')

class Chinese:
    def say_hello(self):
        print('Ni hou')

def intro(lang):
    lang.say_hello()

sarthak = French()
john = Chinese()

intro(sarthak)
intro(john)
