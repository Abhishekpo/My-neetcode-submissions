# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Bfs
        if not root:
            return None
        queue=deque([root])

        while queue:

            for el in range(len(queue)):
                popel= queue.popleft()
                if popel.left:
                    queue.append(popel.left)
                if popel.right:
                    queue.append(popel.right)
                temp=popel.left
                popel.left=popel.right
                popel.right=temp
        return root


        
        


