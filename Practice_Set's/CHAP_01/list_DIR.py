import os

# Specify the directory path (use '.' for the current directory)
directory_path = '.'

# List the contents of the directory
contents = os.listdir(directory_path)

# Print the contents
print("Contents of the directory:")
for item in contents:
    print(item)


# os is a built-in module

"""
1. os.listdir(): This function retrieves the names of all files and directories in the given path.

2. for item in contents: Iterates through the list of items and prints each one.
"""