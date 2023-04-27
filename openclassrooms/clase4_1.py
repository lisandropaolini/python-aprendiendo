import random
 
n = random.uniform(10,19)
print(n)



import random

basket = ["Apple", "Pear", "Banana", "Pineapple", "Orange"]
result = random.choice(basket)
print(result)

result = basket[random.randint(0, 4)]
print(result)

result = random.shuffle(basket)
print(result)
