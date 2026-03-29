# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(root, subRoot):

            if(not subRoot):
                return True
            if(not root):
                return False
            if(root.val==subRoot.val):
                if(isSame(root, subRoot)):
                    return True
            return dfs(root.left, subRoot) or dfs(root.right, subRoot)
        def isSame(r, l):
            if(not r and not l):
                return True
            if(not r or not l):
                return False
            if(r.val!=l.val):
                return False
            return isSame(r.left, l.left) and isSame(r.right, l.right)
        return dfs(root, subRoot)
