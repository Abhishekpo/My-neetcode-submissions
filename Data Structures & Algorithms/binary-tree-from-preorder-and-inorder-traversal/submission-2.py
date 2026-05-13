# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:


        def dfs(preorder, inorder):

            if len(preorder) <=0 or len(inorder) <=0:
                return None

            rootval= preorder[0]
            newnode= TreeNode(rootval)

            mid= inorder.index(rootval) 

        
            leftpart_inorder= inorder[:mid]
            rightpart_inorder = inorder[mid+1:]


            left_preorder = preorder[1:mid+1]
            right_preorder = preorder[mid+1:]

        
            newnode.left= dfs(left_preorder, leftpart_inorder)
            newnode.right =dfs(right_preorder, rightpart_inorder )
        
            return newnode

        return dfs(preorder, inorder)

