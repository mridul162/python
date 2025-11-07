x = input("Enter a num1: ")
y = input("Enter num2: ")

try:
    # z= int(x)/ int(y)
    z= x/ int(y)
# except Exception as e:
#     print('Exception Occurred: ', e)

except ZeroDivisionError as e:
    print('Division by Zero Occurred!')
    z= None
except Exception as e:
    print('Exception type: ', type(e).__name__)
    z= None

print("Division is: ", z)