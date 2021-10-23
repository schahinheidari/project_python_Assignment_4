#Assignment 4

m = int(input("please enter your number: "))
n = int(input("please enter your number: "))

if(m > n):
    max = m
else:
    max = n
for i in range(n, (m*n)+1):
    if(max % m == 0 and max % n == 0):
        print("oyur LCM is:",max)
        break