def outer_function(msg):
    message = msg
    def inner_function():
        print(message)
    return inner_function

hi_func = outer_function('Hi')
bye_func = outer_function('Bye')

hi_func()
bye_func()

    