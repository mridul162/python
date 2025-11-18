# Function with default argument
def sum(a,b=0):
    print("a: ", a)
    print("b: ", b)
    total= a+b      # local variable
    print("Total Inside: ", total) #
    return total  

# Function with multiple return values
def arithmetic_operations(x, y):
    add = x + y
    sub = x - y
    mul = x * y
    div = x / y
    return add, sub, mul, div

# Function with variable number of arguments
def multiply(*args):
    result = 1
    for num in args:
        result = result * num
    return result

# Function with keyword arguments
def person_info(name, age, city):
    print("Name: ", name)
    print("Age: ", age)
    print("City: ", city)
    return