# i = 1
# while i <= 50:
#     print(f"{i:2}", end=" ")  # Ensures all numbers take up 2 spaces

#     if i % 10 == 0:  # Moves to a new line every 10 numbers
#         print()

#     i += 1



for i in range (1,51):
    print(f"{i:2}", end=" ")
    if i % 10 == 0:  # Moves to a new line every 10 numbers
        print()
    i = i+1
