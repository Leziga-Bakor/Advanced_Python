def decorator_function(original_function):
    def wrapper_function():
        print(f'wrapper executed this before {original_function.__name__}')
        return original_function()
    return wrapper_function

def display():
    print('display function ran')

decorated_display = decorator_function(display)
decorated_display()
'''
What is a Decorator?

A decorator is a function that takes another function as an argument. It can perform actions around the function argument without changing structure of original function

'''

