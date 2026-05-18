# 4. Write a python program to print the contents of a directory using the os module. Search
# online for the function which does that.

import os 
cwd = os.getcwd() 
print("Current working directory:", cwd)


path = "/Users/cyborg/Desktop/Python/CwH Python"
dir_list = os.listdir(path) 
print("Files and directories in '", path, "' :") 
print(dir_list)
