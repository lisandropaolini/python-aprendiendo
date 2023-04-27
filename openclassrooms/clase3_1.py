customerName = ['Marion Weaver', 'Alberto Mendoza', 'Katharine Tyler', 'Isaac Steele']

# assign the value 'Marianne Weaver' to the first name in our list
# it is index 0, because indices start at 0 in python!
customerName[0] = 'Marianne Weaver'

print(customerName[0])

# print the last item
print(customerName[-1])

# access the second item to the 3rd
print(customerName[1:3])

# access all items from the beginning to the second
print(customerName[:2])


amountAccount = [10000, 150, 300, 1800.74]

strangeList = [4, 10.2, 'Marion Weaver', ['another list', 1]]

# print the 4th item of the list
print(strangeList[3])


colors = ['red', 'yellow', 'orange', 'green', 'blue']
colors[3] = 'emerald'
for color in colors :
    print(color)


list = []
list.append(7) # -> [7]
list.append(5) # -> [7, 5]
list.insert(1,12) # [7, 12, 5]
list[0] = 4 # -> [4, 12, 5]
list.remove(12) # [4, 5]
list.index(5) # prints 1
list.extend([1, 2, 3]) # [4, 5, 1, 2, 3]
del list[3] # [4, 5, 1, 3]


accounts = {'Marion Weaver': 10000, 'Alberto Mendoza': 150, 'Katharine Tyler': 300, 'Isaac Steele': 1800.74}
print(accounts['Alberto Mendoza']) # -> 150

accounts.pop('Alberto Mendoza') # deletes Alberto Mendoza from our dictionary

len(accounts) # -> 3

my_tuple = (1, 2, 3, 'a', 'b')
print(my_tuple[1]) # -> 2
print(my_tuple[4]) # -> 'b'
a, b = (1, 'apple')
print(a) # -> 1
print(b) # -> 'apple'
