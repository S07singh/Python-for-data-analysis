# Python file detection

import os

# file_path = "test.txt" # relative path file_path = "stuff/test.txt"
# file_path = "C:\\Users\\sudhi\\OneDrive\\Desktop\\test.txt" # absolute path
file_path = "C:/Users/sudhi/OneDrive/Desktop/test.txt" # absolute path

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a folder")

else:
    print("That location doesn't exist")