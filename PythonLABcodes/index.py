# file=open("read.txt","r")
# text = file.read()
# print(text)
# file.close()

# file=open("write.txt","w")
# text = file.write("hey anas this is write.txt")
# print(text)
# file.close()

# file=open("append.txt","a")
# text = file.write("\nappending abcdeg")
# print(text)
# file.close()

# file=open("readnwrite.txt","r+")
# file.write("hey anas this is readnwrite.txt")
# file.seek(0)
# text = file.read()
# print(text)
# file.close()

#WAP to read text from a given file poem.txt and find out where it contains the word twinkle.

# file = open("poem.txt", "r")
# lines = file.readlines()
# for i in range(len(lines)):
#     if "twinkle" in lines[i].lower():
#         print(f"'twinkle' found in line {i+1}: {lines[i].strip()}")
# file.close()

#WAP to make a copy of a text file "this.txt"

f = open("this.txt", "r")

data = f.read()
f.close()

f2 = open("copy.txt", "w")

f2.write(data)
f2.close()

# WAP to mine a log file to find whether it contains the word PYTHON.
#WAP TO FIND OUT THE LINE NUMBER WHERE THE WORD PYTHON IS PRESENT.
#WAP to find out whether the file is identical and matches the content of another file.
#WAP TO WIPE OUT THE CONTENTS OF A FILE USING PYTHON
#WAP TO RENAME A FILE TO "RENAMEBYPYTHON.txt"
#a program contains donkey , WAP to replace that word to "######"