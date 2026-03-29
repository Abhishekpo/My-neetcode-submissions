# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # first print left 
        # 2nd print root 
        # 3rd print right
        ans=[]
        def dfs(root):

            if(root==None):
                return
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)
            return
        dfs(root)
        return ans
