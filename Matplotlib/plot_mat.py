import numpy as np 
import matplotlib.pyplot as plt 

'''
X_data = np.random.random(50) * 100
Y_data = np.random.random(50) * 100

plt.scatter(X_data, Y_data, c="red", s=100, marker='*')
plt.show()

'''

'''
years = [2006 + x for x in range(16)]
weights = [80,83,84,85,86,82,81,79,83,
           83,80,82,82,83,81,79]

plt.plot(years,weights,c='g',lw=3, linestyle = '--')
plt.show()

# NB: line plot is the default plot for matplotlib.pyplot

'''


'''
x = ['C++', 'C#', 'Python', 'Java', 'Go']
y = [20, 50, 140, 1, 45]

plt.bar(x,y, color = 'r', align='edge', width=.8, edgecolor ='g', lw =3)
plt.show()

'''

'''
# Histogram
ages = np.random.normal(20,1.5,1000)
plt.hist(ages, bins=[ages.min(), 18,21,ages.max()])
plt.show()

plt.hist(ages, bins=20,cumulative=True)
plt.show()

'''

# pie chart
langs=['Python','C++','Java','C#','Go']
votes=[50,24,14,6,17]
explodes = [0,0,0,0.2,0]

plt.pie(votes,labels=langs, explode=explodes,
        autopct='%.2f%%', pctdistance=1.3, startangle=90)
plt.show()