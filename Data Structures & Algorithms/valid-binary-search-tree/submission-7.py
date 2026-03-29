# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        curr=root
        def dfs(curr, high, low):
            if(not curr):
                return True
            
            if(curr.val<high):
                if(not dfs(curr.left, curr.val, low)):
                    return False
            else:
                return False
            if(curr.val>low):
                if(not dfs(curr.right, high, curr.val)):
                    return False
            else:
                return False
        
            return True
        
        return dfs(root, float("inf"), float("-inf"))

