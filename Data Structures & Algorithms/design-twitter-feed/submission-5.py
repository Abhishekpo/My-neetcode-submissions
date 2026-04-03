class Twitter:

    def __init__(self):
        self.tweets=defaultdict(list)
        self.followers=defaultdict(set)
        self.time=0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.followers[userId].add(userId)
        self.time -=1
        

    def getNewsFeed(self, userId: int) -> List[int]:

        ans=[]
        maxheap=[]
        for followee in self.followers[userId]:
            for tweet in self.tweets[followee]:
                maxheap.append(tweet)
        heapq.heapify(maxheap)
        while maxheap and len(ans)<10:
            time, tweet= heapq.heappop(maxheap)
            ans.append(tweet)
        return ans


        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            if followerId !=followeeId:
                self.followers[followerId].remove(followeeId)
        
