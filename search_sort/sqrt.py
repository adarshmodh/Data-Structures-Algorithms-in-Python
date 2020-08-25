
# Project 
# Find the sqrt of a number without using swrt, positive integer, 5, - 2.235 , 2. 1.414 

def binary_search(x,y,num,tol):
    mid = (x+y)/2
    if (abs(num - mid**2) <= tol) or mid**2==num:
        return mid
    elif mid**2 < num:
        return binary_search(mid, y, num, tol)
    else:
        return binary_search(x, mid, num, tol)
    

def sqrt(num, tol):
    
    x = 1
    
    while(1):
        if (x*x == num):
            break
        elif (x**2 > num):
            x = binary_search(x-1,x,num, tol)
            break
        else:
            x += 1
    
    return x

input = 5

print(sqrt(2, 0.001))