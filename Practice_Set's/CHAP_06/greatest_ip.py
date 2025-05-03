a = int(input("Enter value for no. a: "))
b = int(input("Enter value for no. b: "))
c = int(input("Enter value for no. c: "))
d = int(input("Enter value for no. d: "))

if a > b and a > c and a > d:
    print("a is the greatest number:",a)

elif b > a and b > c and b > d:
    print("b is the greatest number:",b)

elif c > a and c > b and c > d:
    print("c is the greatest number:",c)

else:
    print("d is the greatest number:",d)




    # error faced: unable to differentiate "&", "and"
    # bitwise AND operator (&)
    # logical AND operator (and)
    