class Trienode:

    def __init__(self):
        self.children=[0]*26
        self.endofString=False

class PrefixTree:

    def __init__(self):
        self.trie=Trienode()
        

    def insert(self, word: str) -> None:
        curr=self.trie
        for c  in word:
            i=ord('a')-ord(c)
            if not curr.children[i]:
                curr.children[i]=Trienode()
            curr=curr.children[i]
        curr.endofString=True
    
            
    def search(self, word: str) -> bool:
        curr=self.trie
        for c in word:
            i=ord('a')-ord(c)
            if curr.children[i]:
                curr=curr.children[i]
            else:
                return False
        if(curr.endofString):
            return True
        return False


    def startsWith(self, prefix: str) -> bool:
        curr=self.trie
        for c in prefix:
            i=ord('a')-ord(c)
            if curr.children[i]:
                curr=curr.children[i]
            else:
                return False
        return True

        
        