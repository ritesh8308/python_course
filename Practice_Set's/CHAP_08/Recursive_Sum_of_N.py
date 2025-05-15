"""When to Use Recursion?
Recursion is ideal when the problem can be naturally divided into smaller subproblems.
 However, if efficiency or memory constraints are a concern, 
 an iterative approach might be a better choice."""

#Risk of Infinite Recursion – If the base case is not properly defined, the recursion may never terminate, leading to an infinite loop.

def sum_natural_numbers(n):
    if n == 1:
        return 1  # Base case: the sum of the first 1 natural number is just 1
    else:
        return n + sum_natural_numbers(n - 1)  # Recursive case

# Example usage
num = int(input("Enter a number: "))
if num > 0:
    result = sum_natural_numbers(num)
    print(f"The sum of the first {num} natural numbers is: {result}")
else:
    print("Please enter a valid Natural Number.")



    """
    for N = 1000

    RecursionError: maximum recursion depth exceeded.

    By default, Python allows around 1000 recursive calls before stopping to prevent excessive memory usage.

    For calculating large sums, the mathematical formula  (n * (n + 1) // 2)  is the fastest and most memory-efficient method.
    """
