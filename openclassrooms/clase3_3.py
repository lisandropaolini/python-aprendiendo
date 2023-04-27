myString = "Items"

for elt in myString:
    print(elt)

for i in range(0, 5, 1):
    print(i) # -> print from 0 to 4 by steps of 1 (end - 1)

for i in range(0, 5):
    print(i) # -> prints from 0 to 4 also (default step is 1)

for i in range(5):
    print(i) # -> prints from 0 to 4 also (default start is 0)

for i in range(0, 5, 2):
    print(i) # -> print 0, 2 then 4


numberTrees = 0

while numberTrees < 10:
    numberTrees += 1
    print("I planted", numberTrees, "trees")

print("I have a nice forest!")

a = ['foo', 'bar', 'baz', 'qux', 'corge']
 
while a:
   if len(a) < 3:
      break
   print(a.pop())
print('Done.')