# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # if not root:
        #     return None
    
        # temp=root.right # or we might just do root.right=root.left, root.left=root.right
        # root.right=self.invertTree(root.left)
        # root.left=self.invertTree(temp)
        
        # return root

        # bfs

        if not root:
            return None

        myqueue=deque([root])
        while myqueue:

            for i in range(len(myqueue)):
                node= myqueue.popleft()
                temp=node.right
                node.right = node.left
                node.left=temp
                if node.left:
                    myqueue.append(node.left)
                if node.right:
                    myqueue.append(node.right)
        return root


        
        
            