# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        


        def dfs(root, upperbound, lowerbound):

            if not root:
             return True
            
            if root.val <= lowerbound or root.val >= upperbound:
             return False
            
            
            if not dfs(root.left,  root.val, lowerbound):
                return False
            if not dfs(root.right, upperbound, root.val):
                return False

            return True

        return dfs(root, float("inf"), float("-inf"))
                
            