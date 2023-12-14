def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f'wrapper executed this before {original_function.__name__}')
        return original_function(*args, **kwargs)
    return wrapper_function

# def display():
#     print('display function ran')

# decorated_display = decorator_function(display)
# decorated_display()

'''
What is a Decorator?

A decorator is a function that takes another function as an argument. It can perform actions around the function argument without changing structure of original function

'''
# @decorator_function
# def display():
#     print('display function ran')

# display()

@decorator_function
def display_info(name, age):
    print('display_info ran with argments {}. {}'.format(name,age))

display_info('john',25)