a = (1, 2, 3)  # Tuple
a.remove(2)  # Attempt to remove an element Fails
print(a)

#The error occurs at a.remove(2), because tuples do not support modification.


'''How to Handle This?
If you need to remove an element from a tuple, you'd have to create a new tuple instead:


a = (1, 2, 3)
a = tuple(x for x in a if x != 2)  # Creating a new tuple without 2
print(a)  # Output: (1, 3)


Alternatively, convert it to a list, modify it, and then convert back:


a = (1, 2, 3)
a_list = list(a)  # Convert to list
a_list.remove(2)  # Remove element
a = tuple(a_list)  # Convert back to tuple
print(a)  # Output: (1, 3)
'''