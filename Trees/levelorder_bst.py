# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder_bfs(self, root: TreeNode) -> List[List[int]]:
        
        output = []
        stack = []

        if root is not None:
            stack.append((1, root))
        
        while stack != []:
            current_depth, root = stack.pop()
            
            if root is not None:
                if len(output) >= current_depth:
                    print(current_depth, root.val)
                    output[current_depth-1].append(root.val)
                else:
                    print(current_depth, root.val)
                    output.append([root.val])

                stack.append((current_depth + 1, root.right))
                stack.append((current_depth + 1, root.left))
         
        return output
    
    def levelOrder_dfs(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        
        def helper(node, level):
            # start the current level
            if len(levels) == level:
                levels.append([])

            # append the current node value
            levels[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
            
        helper(root, 0)
        return levels
