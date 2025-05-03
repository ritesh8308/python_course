# # taking students marks as input :
 
marks = []

def get_valid_input(prompt, min_value, max_value):
    while True:
        try:
            value = float(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input! Please enter a valid Percentage(%).")

# Example usage
print("Please enter  Student's marks  in the range 0-100:")
for i in range(6):
    s_mark = get_valid_input("Enter marks obtained : ", 0.00, 100.00)
    marks.append(s_mark)


#print(marks.sort())
# Prints "None" beacause it only sorts list and does not return any sorted list and returns None
  
# Instead use:
print("Sorted Lists:\n",sorted(marks))  
# will not change the marks list
#sorted(marks), it creates a new sorted list and leaves the original list unchanged.

print("Original Lists:\n" ,marks)