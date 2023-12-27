from matplotlib import pyplot as plt

x = ['C++', 'C#', 'Python', 'Java', 'Go']
y = [20, 50, 140, 1, 45]

plt.bar(x,y, color = 'r', align='edge', width=.8, edgecolor ='g', lw =3)
plt.show()