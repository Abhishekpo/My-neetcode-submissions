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
            
            if not (curr.val<high and curr.val>low):
                return False

            left=dfs(curr.left, curr.val, low)
            right=dfs(curr.right, high, curr.val)
        
            return left and right
        
        return dfs(root, float("inf"), float("-inf"))

