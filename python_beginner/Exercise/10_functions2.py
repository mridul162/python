import math
def circle_calc(r):
    ar = math.pi * (r**2)
    cir = 2 * math.pi * r
    dia = 2*r
    return ar, cir, dia

if __name__ == '__main__':
    radius = float(input("Enter a radius: "))
    area, circumference, diameter = circle_calc(radius)
    print(f"Area: {area},\nCircumference: {circumference},"
          f"\nDiameter: {diameter}")

