class TimeMap:

    def __init__(self):
        self.mydict={}

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mydict:
            self.mydict[key]=[[value, timestamp]]
        self.mydict[key].append([value, timestamp])

        

    def get(self, key: str, timestamp: int) -> str:
        res=""
        if key in self.mydict:
            mylist=self.mydict[key]

            L=0
            R=len(mylist)-1
            while L<=R:
                mid=(L+R)//2
                if mylist[mid][1]==timestamp:
                    return mylist[mid][0]

                elif(mylist[mid][1]< timestamp):
                    res= mylist[mid][0]
                    L =mid+1
                else:
                    R =mid-1
        else:
            return res
        return res



        
