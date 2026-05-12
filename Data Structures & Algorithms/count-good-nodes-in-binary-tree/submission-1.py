# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, maxval):

            if not root:
                return 0

            count = 0
            if root.val  >= maxval:
                maxval = max (maxval, root.val)
                count +=1
        
            left =  dfs(root.left, maxval)
            right = dfs(root.right, maxval)

            return count + left + right 

        return dfs(root, float("-inf"))
                 