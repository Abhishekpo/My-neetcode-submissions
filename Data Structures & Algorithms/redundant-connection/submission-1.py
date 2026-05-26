class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = [i for i in range ( 1+len(edges))]

        rank = [1 for i in range( 1+len(edges))]

        def find(node):

            if parent[node] != node:
                parent[node]= find(parent[node])

            return parent[node]
        
        def height(node):
            return rank[node]
        
        def Union1(node1, node2):

            first = find(node1)
            second = find(node2)
            h1 = height(first)
            h2 = height(second)
            
            if first == second :
                return True
            
            if h1 > h2 :
                parent[second] = first
            elif h1 < h2:
                parent[first] = second
            else:
                parent[second] = first
                rank[first] += rank[second]

            return False
        
        for e1, e2 in edges:
            if Union1(e1, e2):
                return [e1, e2]

            
