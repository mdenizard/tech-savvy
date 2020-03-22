import math

def quadratic(a, b, c):
    discriminant = (b*b) - 4*a*c
    if discriminant>0:
        print("This equation has two real solutions:")
        x1 = (-b + math.sqrt(discriminant))/(2*a)
        x2 = (-b - math.sqrt(discriminant))/(2*a)
        print(x1) 
        print(x2)
    elif discriminant==0:
        print("This equation has one real solution:")
        x1 = (-b + math.sqrt(discriminant))/(2*a)
        print(x1) 
    else:
        print("This equation has no real solution:")


quadratic(5, 6, 1)