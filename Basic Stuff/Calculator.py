#Program to simulate a calculator in Python

def add(x,y):
	print('Addition')
	return x+y

def sub(x,y):
	print('Subtraction')
	return x-y

def mul(x,y):
	print('Multiplication')
	return x*y

def divide(x,y):
	print('Division')
	return x//y # Doing a floor division to get an integer

def switcher(x):
	sw={
	1:"Add",
	2:"Subtract",
	3:"Multiply",
	4:"Divide"
	}
	return sw.get(x,"nothing")

print('Welcome to a Calculator')
print('Enter two nos. followed by the ops you want to do')
x=int(input())
y=int(input())
z=int(input())
if z==1:
	print(add(x,y))
elif z==2:
	print(sub(x,y))
elif z==3:
	print(mul(x,y))
elif z==4:
	print(divide(x,y))

