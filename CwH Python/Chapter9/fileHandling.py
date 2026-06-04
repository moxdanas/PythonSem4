#reading 
# f = open("file1.txt","r")
# text = f.read()
# print(text)
# f.close()

#writing 
# f = open("file1.txt","w")
# text = f.write("This is nice")
# f.close()


#with statement

with open("file1.txt","r") as f:
    text = f.read()

print(text)