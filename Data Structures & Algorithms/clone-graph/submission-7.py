"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        visited = {}

        def dfs(neigh):

            newnode = Node(neigh.val)

            if neigh in visited:
                return visited[neigh]

            visited[neigh] = newnode

            for n in neigh.neighbors:
                newnode.neighbors.append(dfs(n))
            
            return newnode

        if node:
           return dfs(node)

        else:
            return None
        
