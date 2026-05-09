# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs (root, subRoot):

            if not root and not subRoot:
                return True

            if root and not subRoot:
                return False

            if not root and subRoot:
                return False
            
            if root.val != subRoot.val:
                return False
            
            return dfs(root.left, subRoot.left) and dfs(root.right, subRoot.right)

        def isSame (root):

            if not root:
                return False
            
            if not subRoot and root:
                return True
            
            if dfs(root, subRoot):
                return True
            
            return isSame(root.left) or isSame(root.right)

        return isSame(root)
            
