# Initialize an empty set
unique_numbers = set()

# Prompt user for input
print("Enter 8 numbers:")

for _ in range(8):
    num = int(input())  # Convert input to integer
    unique_numbers.add(num)  # Add number to the set

# Display unique numbers
print("Unique numbers:", unique_numbers)
