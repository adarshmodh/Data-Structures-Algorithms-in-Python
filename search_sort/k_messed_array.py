"""
Given an array of integers arr where each element is at most k places away from its sorted position, code an efficient function sortKMessedArray that sorts arr. For instance, for an input array of size 10 and k = 2, an element belonging to index 6 in the sorted array will be located at either index 4, 5, 6, 7 or 8 in the input array.

[what is the length of the heap?]
k+1 = len(heap)
heap [2,4,5]
[1,]
for i in len(arr):
  heappop() -> 1
  heappush(k+1) -> 2
"""

from heapq import heappop,heappush

'''
min_heap = []
heap.heappush(min_heap, x)
heap.heappop(min_heap)
'''

def sort_k_messed_array(arr, k):
  
  tmp = 0
  min_heap = [] 
  
  while(tmp<=k):
    heappush(min_heap,arr[tmp])
    tmp = tmp+1
    
  #print(min_heap)
  
  output = []
  
  for i in range(k+1,len(arr)):
    output.append(heappop(min_heap))
    heappush(min_heap,arr[i])
  
  while(k+1):
    output.append(heappop(min_heap))
    k=k-1
                  
  return output


arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
k = 2
print(sort_k_messed_array(arr,k))

