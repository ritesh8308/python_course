def print_pattern(n):
    for i in range(n,0,-1):   # Decremental loop from n to 1
        print("*" * i)  # prints i  '*'

# customized pattern by taking the i/p from user:
num = int(input("Enter the number of lines to be printed:"))
print_pattern(num)