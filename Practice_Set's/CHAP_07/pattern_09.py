n = int(input("Enter no. of rows:"))

for i in range(n):
    if i == 0 or i == n-1:  # for first and last row
        print("* " * n)
    else:
        print("*"+" " * (2*(n-2))+ " *")
