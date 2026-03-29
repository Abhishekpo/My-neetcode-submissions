"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        oldtonewdic={}

        # def dfs(node):

        #     if node in oldtonewdic:
        #         return oldtonewdic[node]

        #     copy=Node(node.val)
        #     oldtonewdic[node]=copy

        #     for nei in node.neighbors:
        #         copy.neighbors.append(dfs(nei))

        #     return copy

        # return dfs(node) if node else None


        #Bfs
        if not node:
            return None
        queue=deque([node])
        
        while queue:
            curr =queue.popleft()
            if curr not in oldtonewdic:
                copy=Node(curr.val)
                oldtonewdic[curr]=copy
            else:
                copy=oldtonewdic[curr]

            for nei in curr.neighbors:
                if nei not in oldtonewdic:
                 oldtonewdic[nei]=Node(nei.val)
                 queue.append(nei)
                
                copy.neighbors.append(oldtonewdic[nei])

        return oldtonewdic[node]
            




        