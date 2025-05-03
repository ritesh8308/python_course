U_name = str(input("please enter your user_name: "))
char_len = len((U_name))   #unnecessarily memory will be occupied by char_len : refer to the below otimized code
if char_len<10:
    print("given user name contains less than 10 characters")
else:
    print("given user namev \t DO NOT \t contains less than 10 characters") 



    #optimized version of code:


   """ U_name = input("Please enter your username: ")  # No need for `str()` as `input()` returns a string by default.
if len(U_name) < 10:
    print("The given username contains less than 10 characters.")
else:
    print("The given username does NOT contain less than 10 characters.")
"""