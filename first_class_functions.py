'''
First-Class Functions:
"A Programming Languate is said to have first-class functions if it treats functions as first-class citizens"

First-Class Citizens (Programming):
"A first-class citizen (sometimes called first class objects) in a programming language is an entity which supports all the operations generally available to other entities. these operations typically include being passed as an argument, returned from a function and assigned to a variable"

'''

# def square(x):
#     return x * x

# f = square(5)

# print(square)
# print(f)


# # Assigning the function to a variable
# g = square

# print(g)
# print(g(5))

'''
A higher order function accepts a function as an argument or returns a function as a result#

'''

# # A map function that accepts a function as an argument
# def my_map(func, arg_list):
#     result = []
#     for item in arg_list:
#         result.append(func(item))
#     return result

# squares = my_map(square, [1,2,3,4,5])
# print(squares)

# A function that returns a function

# def logger(msg):

#     def log_message():
#         print('log:', msg)
    
#     return log_message


# log_hi = logger('Hi')
# log_hi()

def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag,msg))
    return wrap_text
''
print_h1 = html_tag('h1')
print_h1('Test Headline!')
print_h1('Another Headline')

print_p = html_tag('p')
print_p('Test Paragraph!')