def mult_num(N):
    for i in range(1,11):  # loop from 1 to 10
        print(f"{N} X {i} = {N*i}")

# Taking user i/p number to print it's table:
Num = int(input("Enter a number to print it's table:"))
print()
print(f"table of {Num} is:")
mult_num(Num)