# replacing "  :2" by " :1" spaces
name = "Ritesh  Appasaheb  Mane"
corrected_name = (name.replace("  "," "))
print(corrected_name)

"""

#replacing multiple spaces with " ":

name = "Ritesh  App as  aheb   Ma      ne"

# Replace multiple spaces with a single space
corrected_name = " ".join(name.split())

print(corrected_name)

* name.split() splits the string into a list of words based on whitespace (it automatically handles multiple spaces).

* " ".join() joins the words back together with a single space between them.

"""