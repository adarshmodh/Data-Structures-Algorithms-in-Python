class BST:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        if not self.left and not self.right: # leaf node
            return str(self.data)
        else:
            left_str = str(self.left) if self.left else "_"
            right_str = str(self.right) if self.right else "_"
            return "(" + left_str + " " + str(self.data) + " " + right_str + ")"

    # Returns the nth smallest element of the binary search tree,
    # where n=0 returns the smallest, n=1 returns the second smallest, etc
    # Returns None if there are not n elements in the tree
    
    def nth_smallest(self, n):
        #****************
        # YOUR CODE HERE
        """
        1) go to the smallest element first by traversing through every left subtree
        2) keep track of nodes by storing them in queue while doing that
        3) Pop the nodes one by one and keep reducing value of n
        4) In this way, we are doing an inorder traversal 
        5) Then return the node value once n is below zero (since we start n at zero)

        """
        #****************

        root = self
        queue = []

        while root or queue:
          while root:
            queue.append(root)
            root = root.left
          
          root = queue.pop()
          n = n - 1
          if n < 0:
            return root.data
          root = root.right

        return None    

test_bst = BST(8,
               BST(3,
                   BST(1),
                   BST(6,
                       BST(4),
                       BST(7))),
               BST(10,
                   None,
                   BST(14,
                       BST(13),
                       None)));

print("test_bst = " + str(test_bst))
# test_bst = ((1 3 (4 6 7)) 8 (_ 10 (13 14 _)))

for n in range(0, 9):
    print(str(n) + "th smallest: " + str(test_bst.nth_smallest(n)))

# 0th smallest: 1
# 1th smallest: 3
# 2th smallest: 4
# 3th smallest: 6
# ...
# 8th smallest: 14
# 9th smallest: None
