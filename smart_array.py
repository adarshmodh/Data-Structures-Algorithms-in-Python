# // Implement a class that takes in a array as input
# // A method that can return the sum of elements between two indices
# // The method will be called a lot of times

# // [1,2,3,4,5,6]

# // 0,3 --> 1+2+3+4
# // 1,4 --> 2+3+4+5


"""
cum_sum = [1,3,6,10,15,21]

"""
###########################################
# first version #
class my_array:
    def __init__(self,arr):
        self.arr = arr
    
    def sum_elements(self,i,j):
        # o(n)
        sum_out = 0
        
        for k in range(i,j+1):
            sum_out += self.arr[k] 
            
        return sum_out
###########################################

class smart_array:
    def __init__(self,arr):
        self.arr = arr
        self.cum_sum = [0]
        # sumation = 0
        for i in range(len(arr)):
            tmp = self.cum_sum[i]
            self.cum_sum.append(tmp + self.arr[i])
    
    def sum_elements(self,i,j):
        # o(1)
        return self.cum_sum[j+1] - self.cum_sum[i]    

###########################################      
class smart_array:
    def __init__(self,arr):
        self.arr = arr
        self.cum_sum = [0]
        # sumation = 0
        for i in range(len(arr)):
            tmp = self.cum_sum[i]
            self.cum_sum.append(tmp + self.arr[i])
    
    def sum_elements(self,i,j):
        # o(1)
        return self.cum_sum[j+1] - self.cum_sum[i]
    
    def update(self, key, value):
        old = self.arr[key]
        self.arr[key] = value
        
        diff = value - old
        
        for i in range(key, len(self.arr)):
            self.cum_sum[i+1] += diff
        

arr = [1,2,3,4,5,6]
arr_class = smart_array(arr)
print(arr_class.cum_sum)
print(arr_class.sum_elements(0,3))
arr_class.update(2,0)
print(arr_class.cum_sum)
print(arr_class.sum_elements(0,3))

