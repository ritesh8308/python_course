s = {8, 7, 12, "Harry", [1,2]}  #  This will raise a TypeError

"""
This happens because lists do not have a fixed hash value, making them incompatible with sets.
Sets in Python only allow immutable elements like integers, strings, and tuples.

Lists are mutable, meaning their contents can be changed.

Since sets rely on hashing for fast lookups, they cannot contain mutable elements like lists.
"""

#Alternative Solution:
s = {8, 7, 12, "Harry", (1,2)}  #  Works fine

#Tuples are immutable, so Python allows them inside set