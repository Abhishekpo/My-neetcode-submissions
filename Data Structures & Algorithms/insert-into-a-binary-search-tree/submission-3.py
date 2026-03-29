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
        
        # iterative approach:

        if not root:
            return TreeNode(val)
        curr=root
        while True: # why not while curr because current can be null and we have to keep track of its parent
        # to assign its value but this way we dont have to.
            if val<curr.val:
                if not curr.left:
                    curr.left=TreeNode(val)
                    return root
                curr=curr.left
            else:
                if not curr.right:
                    curr.right=TreeNode(val)
                    return root
                curr=curr.right
        

                
