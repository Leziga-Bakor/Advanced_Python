'''
A closure is a record storing a function together with an environment: a mapping associating each free variable of a function with the value or storage location to which the name was bound when the closure was created. A closure unlike a plain function allows the function to access those captured variables through the closure's reference to them, even when the function is invoked outside their scope.
'''

def outer_func():
    message = 'Hi'
    def inner_func():
        print(message)
    return inner_func

my_func = outer_func()

my_func()
my_func()