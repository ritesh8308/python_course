# Built-in_Module_Used: os
# The os module is part of Python's standard library and doesn't require separate installation.

import os  # Import the os module to work with operating system functionalities.

 #directory changed to "C:/"
directory_path = 'C:/' 
# List the contents of the directory using os.listdir()
# os.listdir() retrieves the names of all files and directories in the specified path.
contents = os.listdir(directory_path)

# Print the contents of the directory
print("Contents of the directory:")
# Loop through each item in the contents list and print them
for item in contents:
    print(item)

"""
Explanation of Key Functions and Code:

1. import os:
   - Imports the os module to enable interaction with the operating system.

2. directory_path = '.':
   - Specifies the path of the directory to be explored. The '.' refers to the current working directory.

3. os.listdir():
   - This function retrieves the names of files and directories in the given path.

4. for item in contents:
   - Loops through the list returned by os.listdir() and prints each file/directory name.
"""
