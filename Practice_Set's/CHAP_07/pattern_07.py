# user i/p:
n = int(input("Enter he numbe rof rows:"))

for i in range(n):
    spaces = " " * (n-i-1)   #Adding spaces for centering
    stars =  "*" * (2*i+1)
    print(spaces + stars)