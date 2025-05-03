# Get user input
name = input("Enter your name: ")

# List of names
names_in_list = ["Sushant", "Soham", "Amol", "Ajinkya", "Om"]

# Check if any name RITESH MANis found in the comment
is_name = any(keyword.lower() in name.lower() for keyword in names_in_list)

# Print result
if is_name:
    print("Entered name is present in list")
else:
    print("Entered name is not present in list")
