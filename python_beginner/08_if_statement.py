# An example of if statement
num = input("Enter a number: ")
num = int (num)
if num%2==0:
    print("Number is even!")
else:
    print("Number is odd!")

# Another example of if statement
indian=["samosa", "daal", "naan"]
chinese=["egg role", "pot sticker", "fried rice"]
italian=["pizza", "pasta", "risotto"]

dish= input("Enter a dish: ")

if dish in indian:
    print("Indian!")
elif dish in chinese:
    print("Chinese!")
elif dish in italian:
    print("Italian!")
else:
    print("Based on little knowledge I have, I don't know which cuisine is this.")