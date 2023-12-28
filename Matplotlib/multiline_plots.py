import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('dark_background')

'''
link for styles

1. https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
2. https://matplotlib.org/stable/tutorials/introductory/customizing.html

'''

stock_a = [100,102,99,101,101,100,102]
stock_b = [90,95,102,104,105,103,109]
stock_c = [110,115,100,105,100,98,95]

plt.plot(stock_a, label='company1')
plt.plot(stock_b, label='Company2')
plt.plot(stock_c, label='Company3')

plt.legend(loc='upper center')
plt.show()


votes = [10,2,5,16,22]
people = ['A', 'B', 'C', 'D', 'E']

plt.pie(votes, labels=None)
plt.legend(labels=people)
plt.show()