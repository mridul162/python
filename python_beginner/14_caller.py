# Caller script to demonstrate importing a module
import modules.area as a
print("I am in caller.py")
area = a.calculate_area(5,6)
print(area)