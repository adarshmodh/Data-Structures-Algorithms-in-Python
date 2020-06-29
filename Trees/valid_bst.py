# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        dfs + recursion
        time complexity - O(N)
        space complexity - O(1)
        """
        
#         if root is None: 
#             return True
        
#         if root.left:
#             if root.left.val < root.val:
#                 self.isValidBST(root.left)
#             else:
#                 return False

#         if root.right:
#             if root.right.val > root.val:
#                 self.isValidBST(root.right)
#             else:
#                 return False
        
#         return True
    
        def helper(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True
            
            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)

