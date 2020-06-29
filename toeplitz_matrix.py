"""
[[1,2,3,4],
 [5,1,2,3],
 [6,5,1,3]]

m,n = rows, cols 


for m-2 to 0:
  cr,cc = m-2,0 
  
  check bounds m-1, n-1 : break
  check value 
  add cr+1 cc+1


for c-2 to 1 
  cr,cc = 0, c-2 
  check bounds m-1, n-1 : break
  check value 
  add cr+1 cc+1
  
"""


def isToeplitz(arr):
  
  nrows,ncols = len(arr), len(arr[0])
  
  for i in range(nrows-2,-1,-1):

    cr, cc = i, 0
    check_val = arr[cr][cc]

    #### checking bounds
    while(0<=cr<nrows and 0<=cc<ncols):
      
      if arr[cr][cc] != check_val:
        return False
    
      cr += 1
      cc += 1
  
  
  for i in range(ncols-2,-1,-1):
    
    cr, cc = 0, i
    check_val = arr[cr][cc]

    #### checking bounds
    while(0<=cr<nrows and 0<=cc<ncols):
      
      if arr[cr][cc] != check_val:
        return False
    
      cr += 1
      cc += 1
    
  return True

arr = [[1,2,3,4],
       [5,1,2,3],
       [6,5,9,2]]

print(isToeplitz(arr))
