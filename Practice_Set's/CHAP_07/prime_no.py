def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
           return False
    return True

num = int(input("enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")