#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'strokesRequired' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY picture as parameter.
#

"""
input:
picture= ["aabba", "aabba", "aaacb"]
output: 5 fills


pseudocode:

counter = 0
for i,j loop iterates through 2d list:
    if picture[i][j] == "a"
        dfs(picture, i,j, "a")
        counter++
        
    if picture[i][j] == "b"
        
    if picture[i][j] == "c"

    
def dfs(picture, i,j, fill)
    check picture bounds:
        check fill
            picture[i][j] = "0"
            dfs(picture, i+1,j, fill)
            
    else:
        return



"""

def strokesRequired(picture):
    # Write your code here
    # print(picture)
    counter = 0
    for i in range(len(picture)):
        for j in range(len(picture[0])):
            if picture[i][j] == "a":
                dfs(picture, i, j, "a")
                counter += 1
            elif picture[i][j] == "b":
                dfs(picture, i, j, "b")
                counter += 1
            elif picture[i][j] == "c":
                dfs(picture, i, j, "c")
                counter += 1              
    
    return counter 
 
def dfs(picture, i, j , fill):
    if i>=0 and j>=0 and i<len(picture) and j<len(picture[0]):
        if picture[i][j] == fill:
            picture[i][j] = "0"
            dfs(picture, i+1, j , fill)
            dfs(picture, i-1, j , fill)
            dfs(picture, i,   j+1 , fill)
            dfs(picture, i,   j-1 , fill)
        else:
            return
    else:
        return 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    picture_count = int(input().strip())

    picture = []

    for _ in range(picture_count):
        picture_item = input()
        picture.append(list(picture_item))

    result = strokesRequired(picture)

    fptr.write(str(result) + '\n')

    fptr.close()
