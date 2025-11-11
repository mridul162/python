# def calculate_area(height=10, base=10, shape="tri"):
#     if shape == "tri":
#         area = 1/2 * base * height
#     elif shape == "rect":
#         area = base * height
#
#     return area
#
# a = calculate_area()
# print(a)

def print_pattern(n):
    for i in range (n):
        s="*"
        for j in range(i):
            s+="*"
        print(s)

print(print_pattern(4))

