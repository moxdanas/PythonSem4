#file Handling

# reading a file
# file = open("data.txt","r")
# print(file.read())
# file.close()

#writing in a file
# file = open("data.txt","w")
# print(file.write("Hello Python"))
# file.close()

#appending in a file 
# file = open("data.txt","a")
# print(file.write("\nNew line added"))
# file.close()


with open("data.txt","r") as file:
    print(file.readlines())


# file.read()       # Reads full file
# file.readline()  # Reads one line
# file.readlines() # Reads all lines as list

# with open("sample3.txt","r") as file:
#     file.readlines("Python File handling example3!")

