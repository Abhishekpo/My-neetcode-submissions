# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        mem={}
        def dfs( root ):

            if not root:
                return 0

            if root in mem:
                return mem[root]
            # rob
            current_rob=root.val

            if root.left:
              current_rob += dfs(root.left.left)
              current_rob += dfs(root.left.right)
            
            if root.right:
                current_rob += dfs(root.right.left)
                current_rob += dfs(root.right.right)
            #not rob

            notrob= dfs( root.left) + dfs(root.right)

            mem[root]= max( current_rob, notrob)

            return max( current_rob, notrob)

        return dfs(root)
            
