a=4

def poly(a, b, c, x):
	return a*x**2 + b*x + c

b=a
b*=a
c=1
result=poly(a,b,c,0)
a+=3
a=0

print(result)
print(a)
print(b)
print(c)
