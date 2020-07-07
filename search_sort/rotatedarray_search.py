"""
Given shiftArr and an integer num, implement a function shiftedArrSearch that finds and returns the index of num in shiftArr. 
If num isn’t in shiftArr, return -1. Assume that the offset can be any value between 0 and arr.length - 1.

input:  shiftArr = [9, 12, 17, 2, 4, 5], num = 2 # shiftArr is the
                                                 # outcome of shifting
                                                 # [2, 4, 5, 9, 12, 17]
                                                 # three times to the left

output: 3 # since it’s the index of 2 in arr


Time = O(log((N))
Space = O(1)

"""

def shifted_arr_search(shiftArr, num):
    n = len(shiftArr)
    pivot = findPivotPoint(shiftArr)

    if(pivot == 0 or num < shiftArr[0]):
        return binarySearch(shiftArr, pivot, n-1, num)
    
    return binarySearch(shiftArr, 0, pivot - 1, num)


def findPivotPoint(arr):
    begin = 0
    end = len(arr) - 1

    while (begin <= end):
        mid = begin + int((end - begin)/2)
        if (mid == 0 or arr[mid] < arr[mid-1]):
            return mid
        if (arr[mid] > arr[0]):
            begin = mid + 1
        else:
            end = mid - 1

    return 0


def binarySearch(arr, begin, end, num):
    while (begin <= end):
        mid = begin + int((end - begin)/2)
        if (arr[mid] < num):
            begin = mid + 1
        elif (arr[mid] == num):
            return mid
        else:
            end = mid - 1

    return -1


shiftArr = [9, 12, 17, 2, 4, 5]
num = 2

# shiftArr = [0,1,2,3,4,5]
# num = 1

print(shifted_arr_search(shiftArr,num))