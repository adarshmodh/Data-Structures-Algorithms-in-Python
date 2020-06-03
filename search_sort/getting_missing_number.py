"""
input arr = [0, 1, 2, 3], output = 4
input arr = [1, 2, 3], output = 0

3 solutions:

Time complexity O(n logn) and space complexity O(n) ; without arr modification
  sort the array and copy it into new array sorted_arr
  iterate through the new array to look for sorted_arr[i] != i

Time complexity O(n) and space complexity O(n) ; without arr modification
  build a set from the arr
  iterate through the set to find number which is not present

Time complexity O(n) and space complexity O(1) ; with arr modification
  in place sorting like bubble sort or insertion sort 
  iterate through the new array to look for sorted_arr[i] != i

bubble sort:

    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 

"""

solution = 3

def get_different_number(arr):
  n = len(arr)
  
  if solution == 1:
    sorted_arr = list(arr)
    sorted_arr.sort()
    
    for i in range(n):
      if sorted_arr[i] != i:
        return i
    
  elif solution == 2:
    arr_set = set(arr)
    for i in range(n):
      if not i in arr_set:
        return i
    
  elif solution == 3:
    
    #arr.sort()          #inplace sorting
    
    for i in range(n-1): 
      for j in range(0, n-i-1): 
        if arr[j] > arr[j+1] : 
            arr[j], arr[j+1] = arr[j+1], arr[j] 
    
    for i in range(len(arr)):
      if arr[i] != i:
        return i     

  return len(arr)   
  
  
