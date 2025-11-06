# def double(x):
#     return x*2
# print(double(3))

double = lambda x: x*2
cube = lambda x: x**3
avg = lambda x, y: (x+y)/3

print(double(5))
print(cube(3))
print(avg(3,9))

def appl(func, value):
    return func(value)+6

print(appl(lambda x: x**3, 3))