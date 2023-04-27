a = 7.5
b = 3
c = a/b
print(c)
# this will print 2.5, which is a float

a = 10
b = 5
c = a/b
print(c)
# it's a float


a = 14.0
# a is a float
a = int(a)
print(a)
# a is now an integer: it prints 14 and not 14.0

favoriteCityOne = "San Francisco"
favoriteCityTwo = "New York"
favorites = favoriteCityOne + favoriteCityTwo
print(favorites) # => "San FranciscoNew York"

favoriteCityOne = "San Francisco"
favoriteCityTwo = "New York"
favorites = "My favorite cities are " + favoriteCityOne + " and "+ favoriteCityTwo
print(favorites) # -> "My favorite cities are San Francisco and New York"

city = "Sydney"
numberTrips = 5
history = "I've been to " + city + " " + str(numberTrips) + " times "
print(history) # => "I've been to Sydney 5 times"

