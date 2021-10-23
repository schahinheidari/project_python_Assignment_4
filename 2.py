#Assignment 4
import math
a = int(input())
b = int(input())
c = int(input())

def delta(a,b,c):
    delta = b**2 - 4*a*c
    return delta

D = delta(a, b, c)

if D < 0 :
    print("we don't have a answer")
elif D == 0:
    print(D)
else:
    print((-b + math.sqrt(D)) / (2 * a))

    print((-b - math.sqrt(D)) / (2 * a))