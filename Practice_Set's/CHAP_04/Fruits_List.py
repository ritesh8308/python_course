
fruits = []  # Creating an empty list

# Prompting the user to enter seven fruit names
for i in range(7):  # Loop to get seven inputs
    fruit = input(f"Enter fruit {i+1}: ")  # Asking for input
    fruits.append(fruit)  # Adding the fruit to the last index of lists

# Printing the final list of fruits
print("List of fruits:", fruits)

