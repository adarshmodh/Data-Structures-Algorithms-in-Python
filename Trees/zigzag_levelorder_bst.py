# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root: 
            return []
        
        output = []
        temp = []
        stack = [root]
        flag = 1
        
        while stack:
            for i in range(len(stack)):
                node=stack.pop(0)
                temp+=[node.val]
                if node.left: 
                    stack+=[node.left]
                if node.right: 
                    stack+=[node.right]
            
            output+=[temp[::flag]]
            temp=[]
            flag*=-1
        
        return output
