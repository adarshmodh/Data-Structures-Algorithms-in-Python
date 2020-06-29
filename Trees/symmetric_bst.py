# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric_dfs(self, root: TreeNode) -> bool:
        
        def helper(t1,t2):
            if t1 == None and t2 == None:
                return True
            if t1 == None or t2 == None:
                return False
            
            return (t1.val == t2.val) and helper(t1.right, t2.left) and helper(t1.left, t2.right)
        
        if root and root.right and root.left:
            return helper(root.left, root.right)
        
        elif not root :
            return True
        
        elif not (root.right or root.left):
            return True
        
        return False
    
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False
        return True
