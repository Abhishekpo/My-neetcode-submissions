# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        # I thik I have to swap it to the left most child 
        # and delete the child
        curr=root
        def dfs( root, key ):

            if not root:
                return None
            
            if root.val > key:
                root.left = dfs(root.left, key )
            
            elif root.val < key:
                root.right = dfs( root.right, key)
            
            else:
                if not root.left:
                    return root.right

                if not root.right:
                    return root.left

                
                child=root.right
                while child.left:
                    child = child.left

                root.val = child.val

                root.right = dfs(root.right, child.val)

            return root

        
        return dfs(root, key)

            
        

        