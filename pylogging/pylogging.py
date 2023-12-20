import logging
import pylogging2

"""
Logging Levels

1. Debug: Detailed information, typically of interest only when diagnosing problems.
2. INFO: Confirmation that things are working as expected.
3. WARNING: An indication that somethin unexpected happened, or indicative of some problem in the near future (e.g. 'disk space low'). The software is still working as expected.
4. ERROR: Due to a more serious problem, the software has not been able to perform some function.
5. CRITICAL: A serious error, indicating that the program itself may be unalbe to continue running.

default loggin level is Warning: it logs out warnings and higher
"""

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('test.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


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

num_1 = 20
num_2 = 10

add_result = add(num_1, num_2)
logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logger.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multliply(num_1, num_2)
logger.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logger.debug('div: {} / {} = {}'.format(num_1, num_2, div_result))
