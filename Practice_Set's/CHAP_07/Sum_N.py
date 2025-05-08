# # TAKING INPUT FROM THE USER:
# n = int(input("enter a number: "))

# #Initializing varaible values :
# sum_n = 0
# i = 1

# # Using while loop to sum the numbers:
# while i<=n:
#     sum_n += i  # adding current natural number to sum
#     i += 1      # Increment Counter : to next number

# # Displaying the result:
# print(f"The sum of first {n} natural numbers is: {sum_n}")




# WITH FOR LOOP:

n = int(input("enter a number: "))

sum_n = 0
i = 1

for i in range(1,n+1):
    sum_n = sum_n+i
   
   
   # i += 1 
   # #:for loop automatically increments i in each iteration, so you don't need:
  #This won't break your code, but it's redundant and unnecessary.


print(f"The sum of first {n} natural numbers is: {sum_n}")



