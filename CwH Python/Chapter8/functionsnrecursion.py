# def function1():
#     print("hello")

# function1()

# def greet(name):
#     print("Good day",name)

# greet("anas")

# def greet(name = "stranger"):
#     #function body
#     print(name)


# greet()
# greet("harry")


##RECURSION


def factorial(n):
    if n ==0 or n == 1:
        return 1
    
    else: 
        return  n * factorial(n-1)

print(factorial(4))
