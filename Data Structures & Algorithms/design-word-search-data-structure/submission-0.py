class Trienode:
    def __init__(self):
        self.children=[None]*26
        self.endofWord=False

class WordDictionary:

    def __init__(self):
        self.trie=Trienode()

    def addWord(self, word: str) -> None:
        curr=self.trie
        for c in word:
            i=ord("a")-ord(c)
            if not curr.children[i]:
                curr.children[i]=Trienode()
            curr=curr.children[i]
        curr.endofWord=True
        
    def search(self, word: str) -> bool:
        def dfs(i, root):
            if root is None:        # FIX: handle None
                return False
            curr=root
            for j in range(i, len(word)):

                if word[j]==".":
                    for child in curr.children:
                        if dfs(j+1, child):
                            return True
                    return False
                else:
                    k=ord("a")-ord(word[j])
                    if(not curr.children[k]):
                        return False
                    curr=curr.children[k]

            return curr.endofWord
        return dfs(0, self.trie)
            
                    


        

    