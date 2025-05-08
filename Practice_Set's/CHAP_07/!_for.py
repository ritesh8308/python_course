a = int(input("Please enter a no. to find it's factorial: "))
f = 1

for i in range(1,a+1):
    f *= i
    

print(f"the factorial of {a} is: {f}")

num = f
print(f"factorial of a number is of ",len(str(num)),"digits")