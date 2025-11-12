# An example of if-else statement
num = input("Enter a number: ")
num = int (num)

if num%2==0:    # Check if number is even
    print("Number is even!")
else:           # If number is not even, it is odd
    print("Number is odd!")

# An example of if-elif-else statement
indian=["samosa", "daal", "naan"]
chinese=["egg role", "pot sticker", "fried rice"]
italian=["pizza", "pasta", "risotto"]

dish= input("Enter a dish: ")

if dish in indian:      # Check if dish is in indian cuisine
    print("Indian!")
elif dish in chinese:   # Check if dish is in chinese cuisine
    print("Chinese!")
elif dish in italian:   # Check if dish is in italian cuisine
    print("Italian!")
else:                   # If dish is not in any cuisine   
    print("Based on little knowledge I have, I don't know which cuisine is this.")

# An example of nested if statement
age = input("Enter your age: ")
age = int(age)
if age>=18:                     # Check if age is 18 or more
    print("You are eligible to vote.")
    citizen= input("Are you an Bangladeshi citizen? (yes/no): ")
    if citizen.lower() == "yes":   # Check if citizen is Bangladeshi
        print("You can vote in Bangladeshi elections.")
    else:
        print("You cannot vote in Bangladeshi elections.")
else:
    print("You are not eligible to vote yet.")

