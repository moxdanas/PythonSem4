""" 
word="amazing"
print(word[1:6:2])
print(word[:7])
# print(word[:0])
print(len("python"))
str = "my bin laden bin abu bin ahad bin akram bin"
print(str.endswith("bin"))
print("a appears:",str.count("a"))
print(str.capitalize())
print(str.find("bin"))
print(str.replace("bin","ben10"))
print("hey\ni_am\nabc\nthanks")
str1 = "my  name  is  anas"
print(str1)
print(str1.replace("  "," "))

# python lists are containers to store a set of valuese of any dataTypes

list = []
list1 = [7,True,"jamia homdord"]
print(list1)
print(list1[0],"\n",list1[1],"\n",list1[2])
print(list1[0:2])
list2= [5,4,3,2,1]
list2.sort()
print(list2)
list2.reverse()
print(list2)
list2.append(6)
print(list2)
list2.insert(3,8)
print(list2)
list2.pop(3)
print(list2)
list2.remove(6)
print(list2)

"""

# tuple is an immutable datatype in python

# tuple= ()
# tuple1 = (1,1,1,2,3)
# tuple2 = (5,2,"anas")
# print(tuple)
# print(tuple1)
# print(tuple2)
# print(tuple1.count(1))
# print(tuple1.index(1))

# WAP to count the number of zeros in the tuple that is given
# tuple0 = (0,0,0,0,0,0,0,0,0,0,0,0,0)
# print(tuple0.count(0))

#WAP to accept marks of six students and display them in a sorted manner 

# marksList = []
# marks =  int(input("enter marks:"))
# marksList.append(marks)
# print(marksList)
# marks =  int(input("enter marks:"))
# marksList.append(marks)
# print(marksList)
# marks =  int(input("enter marks:"))
# marksList.append(marks)
# print(marksList)
# marks =  int(input("enter marks:"))
# marksList.append(marks)
# print(marksList)
# marks =  int(input("enter marks:"))
# marksList.append(marks)
# print(marksList)


sumList = [1,2,3,4]
sum = sumList[0]+sumList[1]+sumList[2]+sumList[3]
print(sum)