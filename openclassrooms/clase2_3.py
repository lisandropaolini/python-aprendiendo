def printPerimeter():
    dimension1 = 6
    dimension2 = 4
    dimension3 = 3
    perimeter = dimension1 + dimension2 + dimension3
    print(perimeter)

printPerimeter() # => 13



def printPerimeter(dimension1, dimension2, dimension3):
    perimeter = dimension1 + dimension2 + dimension3
    print(perimeter)

printPerimeter(10, 11, 4) # => 25
printPerimeter(2, 2, 3.5) # => 7.5


def calculatePerimeter(dimension1, dimension2, dimension3):
    perimeter = dimension1 + dimension2 + dimension3
    return perimeter

perimeter1 = calculatePerimeter(6, 4, 3)
perimeter2 = calculatePerimeter(10, 3, 11)

print("The perimeter of my first triangle is", perimeter1, "and that of my second is", perimeter2)