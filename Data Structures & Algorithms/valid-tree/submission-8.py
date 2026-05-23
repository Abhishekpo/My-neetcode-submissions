class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        current_path = set()

        mydict = {i:[] for i in range(n)}

        for parent, child in edges:
            mydict[parent].append(child)
            mydict[child].append(parent)
        
        def dfs(node, parent):

            if node in current_path:
                return False
            
            current_path.add(node)

            for child in mydict[node]:
                 if child != parent:
                  if not dfs(child, node):
                     return False

            return True

        
        
        
        return dfs(0, n+1) and len(current_path) == n 
        
