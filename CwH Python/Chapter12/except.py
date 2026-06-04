# try:
#     a = int(input("Enter number: "))
#     b = int(input("Enter number: "))

#     print(a / b)

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# except ValueError:
#     print("Please enter valid integers")



try:
    num = int(input("Enter number: "))
    print(num)

except ValueError:
    print("Invalid input")

else:
    print("Program executed successfully")