# 5. Label the program written in problem 4 with comments.

# Import the os module
import os

# "." means current directory
path = "."

# os.listdir() returns a list of files and folders
contents = os.listdir(path)

# Print heading
print("Contents of the directory:")

# Loop through each item in the directory
for item in contents:
    print("--->",item)

