# # taking subjects marks as input :
# print("please enter marks of subjects in the range 0-100:")
# s1 = int(input("Enter marks obtained in subject S1: "))
# s2 = int(input("Enter marks obtained in subject S2: "))
# s3 = int(input("Enter marks obtained in subject S3: ")) 

def get_valid_input(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

# Example usage
print("Please enter marks of subjects in the range 0-100:")
s1 = get_valid_input("Enter marks obtained in subject S1: ", 0, 100)
s2 = get_valid_input("Enter marks obtained in subject S2: ", 0, 100)
s3 = get_valid_input("Enter marks obtained in subject S3: ", 0, 100)

print(f"Marks entered: S1 = {s1}, S2 = {s2}, S3 = {s3}")


sum =int((s1+s2+s3))

p =float(sum/3)

if p>40 and s1>33 and s2>33 and s3>33:
    print("\ncongratulations you're: \tPassed:",p)
else:print("\nBetter luck next time you're: \t Failed")  # missed writing print stmt for else block of the code:

