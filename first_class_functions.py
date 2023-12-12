'''
First-Class Functions:
"A Programming Languate is said to have first-class functions if it treats functions as first-class citizens"

First-Class Citizens (Programming):
"A first-class citizen (sometimes called first class objects) in a programming language is an entity which supports all the operations generally available to other entities. these operations typically include being passed as an argument, returned from a function and assigned to a variable"

'''

def square(x):
    return x * x

f = square(5)

print(square)
print(f)


# Assigning the function to a variable
g = square

print(g)
print(g(5))

'''
A higher order function accepts a function as an argument or returns a function as a result#

'''

# A map function
def my_map(func, arg_list):
    result = []
    for item in arg_list:
        result.append(func(item))
    return result

squares = my_map(square, [1,2,3,4,5])
print(squares)