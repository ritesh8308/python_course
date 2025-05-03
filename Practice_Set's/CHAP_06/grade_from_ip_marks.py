
def get_valid_input(prompt, min_value, max_value):
    
    while True:
        try:
            value = float(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input! Please enter a valid percentage.")

# 
print("Please enter marks in the range 0-100:")
p = get_valid_input("Enter marks obtained in percentage on Score card: ", 0, 100)


print("Marks entered: ",p)


if 90<p<=100:
    print("You've got \tGrade:Ex")

elif 80<p<=90:
    print("You've got \tGrade:A")

elif 70<p<=80:
    print("You've got \tGrade:B")

elif 60<p<=70:
    print("You've got \tGrade:C")

elif 50<p<=60:
    print("You've got \tGrade:D")

else:
    print("You've got \tGrade:F")

