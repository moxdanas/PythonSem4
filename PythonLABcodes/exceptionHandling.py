#exception handling

try:
    x = int(input("Enter a number: "))
    print(10 / x)
except :
    print("Something went wrong!")
finally:
    print("finally block executed!")

for i in range(1,11,):
    print(i)


# a =330
# b= 4000
# try:{
# if a>b:
#     print(a)
# elif a==b:
#     print("=")
# else:
#     print(b)
# }
# c = 0 if a>b else 0:
# print(c)







#enumerate

# marks = [6,4,3,99,98]
# for(index,m) in enumerate(marks):
#     # print(m)
#     print(index,m)
#     if index == 3 :
#         print("awesome")


a = 10
b=0

try:
    print(a/b)
except ZeroDivisionError:
    print("infinite !")
