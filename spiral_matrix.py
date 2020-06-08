"""
input:  inputMatrix  = [ [1,    2,   3,  4,    5],
                         [6,    7,   8,  9,   10],
                         [11,  12,  13,  14,  15],
                         [16,  17,  18,  19,  20] ]

"""
def spiral_copy(matrix):
  result = []
  rows = len(matrix)
  top_row = 0
  btm_row = rows - 1
  left_col = 0
  right_col = len(matrix[0]) - 1
  
  if rows == 0:
    return result
  
  while(top_row <= btm_row and left_col <= right_col):
    for i in range(left_col, right_col+1):
      result.append(matrix[top_row][i])
    
    top_row += 1
    
    for i in range(top_row,btm_row+1):
      result.append(matrix[i][right_col])
    
    right_col -= 1
      
    if top_row <= btm_row:  
      for i in range(right_col,left_col-1, -1):
        result.append(matrix[btm_row][i])
    
    btm_row -= 1
    
    if left_col <= right_col:
      for i in range(btm_row, top_row-1, -1):
        result.append(matrix[i][left_col])
    
    left_col += 1
  
  return result
  
inputMatrix  = [ [1,    2,   3,  4,    5],
                         [6,    7,   8,  9,   10],
                         [11,  12,  13,  14,  15],
                         [16,  17,  18,  19,  20] ]

 
print(spiral_copy(inputMatrix))
