def add(x,y):
    """ Add Function """
    return x + y

def subtract(x,y):
    """ Subtract Function """
    return x - y

def multliply(x,y):
    """ Multiply Function """
    return x*y 

def divide(x,y):
    """ Divide Function """
    return x/y

num_1 = 10
num_2 = 5

add_result = add(num_1, num_2)
print('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
print('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mult_result = multliply(num_1, num_2)
print('Mul: {} * {} = {}'.format(num_1, num_2, mult_result))

