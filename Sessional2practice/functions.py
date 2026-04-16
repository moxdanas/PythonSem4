#functions

def greet():
    print("hello!")

greet()

# functions with parameters

def greet(name,age,food):
    print("hello",name,"age",age,"fav food",food)

greet("anas","19","biryani")

# function with return value
def add(a,b):
    return a+b
result = add(3,4)
print(result)

#types of functions
#1. built in functions
# print()
# len()
# sum()

# 2. user defined functions
#default functions created by user + lambda functions

#lambda functions(short function)
# square = lambda x: x*x
# print(square(5))

