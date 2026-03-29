class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
     my_map=defaultdict(list)
     for src, dest in edges:
         my_map[src].append(dest)
         my_map[dest].append(src)
    
     visit=set()

     def dfs(node, parent):
         if(node in visit):
             return False

         visit.add(node)

         for nei in my_map[node]:
            if parent == nei:
                continue
            if( not dfs(nei, node)):
                return False
         return True
    
     
     return dfs(0, -1) and n==len(visit)