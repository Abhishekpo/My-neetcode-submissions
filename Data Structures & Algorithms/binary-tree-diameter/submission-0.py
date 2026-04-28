# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxval=[0]
        def dfs(root):

            if not root:
                return 0

            leftval=dfs(root.left)
            rightval=dfs(root.right)

            maxval[0]=max(maxval[0], leftval+rightval)

            return 1 + max(leftval, rightval)

        dfs(root)
        return maxval[0]