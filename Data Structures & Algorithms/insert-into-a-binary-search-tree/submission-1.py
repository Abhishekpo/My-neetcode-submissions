# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        # one way is to travers the tree and find go to the root node and add there
        # another way is to replace the root node
        
        curr=root
        def dfs(curr, val): # this is the recursice approach

            if(not curr):
                return TreeNode(val)

            if (val<curr.val):
                curr.left=dfs(curr.left, val)
            else:
                curr.right=dfs(curr.right, val)

            return curr

        return dfs(curr, val)
                
