def inch_to_cm(Inches):
    cm = float(Inches*2.54)
    return cm

# taking length in Inches :

Inches = float(input("please enter the length in inches scale:"))
cm =inch_to_cm(Inches)
print(f"{Inches}INCH is equal to the {cm}CM")

