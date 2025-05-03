# comment = input("Enter you text:")
# """
# spam keywords:  Make a lot of money,  buy now,  Subcribe this,  click this
# """
# index = comment.find("Make a lot of money",  "buy now",  "Subcribe this",  "click this")  # find accepts only one string: we are passing 4 here@ error

# if 0 <= index < len(comment):
#     print("This is a Spam: SPAMING!!!!")
# else:print("not a SPAM:")


"""
Key Fixes:
Use a List for Spam Keywords: The spam keywords are stored in a list called spam_keywords.

Case Insensitivity: The lower() method is used on both the comment and the keywords to make the check case-insensitive.

Check Using any(): The any() function iterates through the list of spam keywords and checks if any of them exist in the comment.

Improved Logic: Replaced the incorrect usage of find() with an efficient keyword check using in.
"""

# optimised code

# Get user input
comment = input("Enter your text: ")

# List of spam keywords
spam_keywords = ["Make a lot of money", "buy now", "Subcribe this", "click this"]

# Check if any spam keyword is found in the comment
is_spam = any(keyword.lower() in comment.lower() for keyword in spam_keywords)

# Print result
if is_spam:
    print("This is Spam: SPAMMING!!!!")
else:
    print("Not a SPAM.")
