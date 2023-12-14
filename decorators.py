def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

def decorator_function(message):
    def wrapper_function()
        print(message)
    return wr 

hi_func = outer_function('Hi')
bye_func = outer_function('Bye')

hi_func()
bye_func()

'''
What is a Decorator?

A decorator is a function that takes another function as an argument. It can perform actions around the function argument without changing structure of original function

'''

