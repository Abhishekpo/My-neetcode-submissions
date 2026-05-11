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

        queue = deque()
        queue.append(root)
        ans=[]

        while queue:
            current=[]
            for i in range(len(queue)):
                pop= queue.popleft()
                if pop.left:
                    queue.append(pop.left)
                if pop.right:
                    queue.append(pop.right)
                current.append(pop.val)
            ans.append(current)

        return ans

                



