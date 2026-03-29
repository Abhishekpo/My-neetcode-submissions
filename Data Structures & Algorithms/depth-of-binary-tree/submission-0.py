# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        myqueue =deque([root])
        depth=0
        while myqueue:
            for i in range(len(myqueue)):
             node = myqueue.popleft()
             if node.left:
                myqueue.append(node.left)
             if node.right:
                myqueue.append(node.right)
            depth +=1
        return depth
            
        