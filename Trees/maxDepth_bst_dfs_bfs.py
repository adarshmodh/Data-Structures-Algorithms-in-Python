
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:

    def maxDepth_dfs(self, root: TreeNode) -> int:
        """
        dfs + recursion solution
        Time complexity : O(N)
        Space complexity : O(N) (memory required for stack call of recursion)
        """
        if root is None: 
            return 0 
        else: 
            left_height = self.maxDepth_dfs(root.left) 
            right_height = self.maxDepth_dfs(root.right) 
            return max(left_height, right_height) + 1 
        
    def maxDepth_bfs(self, root: TreeNode) -> int:
        """
        bfs solution
        Time complexity : O(N)
        Space complexity : O(log(N)) average case
        """
        stack = []
        if root is not None:
            stack.append((1, root))
        
        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))
        
        return depth


