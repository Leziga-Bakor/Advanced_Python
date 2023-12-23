
'''
my_list = [1,2,3,4,5]

for i in my_list:
    print(i)
    if i == 3:
        break
else:
    print('Hit the for/else statement')

'''

'''
i = 1
while i <= 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print('Hit the while/Else statement')
'''

'''
else after a loop can be seen as no break. It executes only when the loop dosent meet a break statement

'''
def find_index(to_search, target):
    for i, value in enumerate(to_search):
        if value == target:
            break
    else:
        return -1
    return i

my_list = ['Jack', 'John', 'Wick']
index_location = find_index(my_list, '55')

print('Location of target is index: {}'.format(index_location))