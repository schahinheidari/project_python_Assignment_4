#Assignment 4
m = int(input("please inter your first number: "))
n= int(input("please inter your second number: "))

for i in range(n, m+1):
    if(m % i == 0 and n % i == 0):
        gcd = i

print("your Greatest common divisor is:", gcd)