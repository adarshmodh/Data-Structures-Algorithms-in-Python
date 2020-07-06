"""
n - str
m - arr


O(m)

input:  arr = ['x','y','z'], str = "xyyzyzyx"
output: "zyx"


counter of arr

counter of sub x:1 y:2 

 if 

xyyzyzyx
       l
       r

o(2n)  O(n)


"""

from collections import Counter

def get_shortest_unique_substring(arr, string):

    headIndex = 0
    result = ""
    uniqueCounter = 0
    countMap = {}

    for key in arr:
        countMap[key] = 0

    # scan str
    for tailIndex in range(len(string)):
        # handle the new tail
        tailChar = string[tailIndex]

        # skip all the characters not in arr
        if tailChar not in countMap:
            continue

        tailCount = countMap[tailChar]
        if (tailCount == 0):
            uniqueCounter = uniqueCounter + 1

        countMap[tailChar] = tailCount + 1

        # push head forward
        while (uniqueCounter == len(arr)):
            tempLength = tailIndex - headIndex + 1
            if (tempLength == len(arr)):
                # return a substring of str from
                # headIndex to tailIndex (inclusive)
                return string[headIndex:tailIndex+1]

            if (result == "" or tempLength < len(result)):
                # return a substring of str from
                # headIndex to tailIndex (inclusive)
                result = string[headIndex:tailIndex+1]

            headChar = string[headIndex]

            if headChar in countMap:
                headCount = countMap[headChar] - 1
                if (headCount == 0):
                    uniqueCounter = uniqueCounter - 1
                countMap[headChar] = headCount

            headIndex = headIndex + 1

    return result         


arr = ['d','a','n','s'] 
string = "dnajkdnajfdnasjn"

print(getShortestUniqueSubstring(arr, string))