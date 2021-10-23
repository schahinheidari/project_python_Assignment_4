#Assignment 4

m = int(input())
n = int(input())

for i in range(0, m):
        for j in range(0, n):
            if (i+j) % 2 == 0:
                print("*", end=" ")
            else:
                print("#", end=" ")
        print("")


        
