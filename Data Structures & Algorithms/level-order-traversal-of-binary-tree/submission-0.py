# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
         return []

        res=[]
        myqueue=deque([root])

        while myqueue:
            listlevel=[]
            for i in range(len(myqueue)):
                node=myqueue.popleft()
                if node.left:
                    myqueue.append(node.left)
                if node.right:
                    myqueue.append(node.right)
                listlevel.append(node.val)
            res.append(listlevel)

        return res
