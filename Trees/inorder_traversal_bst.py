# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal_dfs(self, root: TreeNode) -> List[int]:
        
        output = []
        
        def helper(root):
            if root is not None:
                if root.left is not None:
                    helper(root.left)
            
                output.append(root.val)        
                
                if root.right is not None:
                    helper(root.right)
            else:
                return 
        
        helper(root)
        return output
    
    def inorderTraversal_bfs(self, root: TreeNode) -> List[int]:
        
        output = []
        stack = []
        
        while root is not None or stack!=[]:
            
            while root is not None:
                stack.append(root)
                root = root.left
           
            root = stack.pop()
            output.append(root.val)
            root = root.right
            
        return output
    
