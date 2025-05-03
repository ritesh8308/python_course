# Create an empty dictionary
fav_languages = {}

#Take input:
for i in range(4):
    name = input("Enter your name: ")
    language = input("Enter your favourite language: ")
    fav_languages[name] = language #Store in dictionary

# display the dictionary o/p:
print("\nFavourite Languagges:", fav_languages)


"""
What happens if two friends have the same name?
Dictionaries in Python do not allow duplicate keys.

If two friends enter the same name, the latest input will overwrite the previous value.
"""

fav_languages = {'Ritesh': 'Python', 'Ritesh': 'Java'}
print(fav_languages)  # {'Ritesh': 'Java'}

#Only the last value remains ('Java'), and 'Python' is lost

"""
What happens if two friends choose the same language?
Dictionaries allow duplicate values, but keys remain unique.

If two friends enter the same favorite language, it will not affect the dictionary's behavior.
"""
fav_languages = {'Ritesh': 'Python', 'Sohan': 'Python'}
print(fav_languages)  # {'Ritesh': 'Python', 'Soham': 'Python'}

#The dictionary stores both names separately, even though they have the same favorite language.