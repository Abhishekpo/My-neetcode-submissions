class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack=[]
        cur=""
        # note: we treat ... and ..... any numbers of dots as valid directly names.
        for p in path+"/": # appending "/" helps to itterate upto the end
            if p=="/":
                if cur== "..":
                    if stack:
                        stack.pop()
                elif cur !="" and cur !=".":
                    stack.append(cur)
                cur=""
            else:
                cur +=p

        return "/"+"/".join(stack)
            

                
                