class Twitter:

    def __init__(self):
        self.count = 0
        self.followerMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        
        min_heap = []
        
        targets = list(self.followerMap[userId])
        if userId not in self.followerMap[userId]:
            targets.append(userId)
        
        for target in targets:
            for count, tweetId in reversed(self.tweetMap[target]):
                if len(min_heap) == 10 and min_heap[0][0] > count:
                    break
                if len(min_heap) == 10 and min_heap[0][0] < count:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, [count, tweetId])
                    continue
                if len(min_heap) < 10:
                    heapq.heappush(min_heap, [count, tweetId])
                
        res = []
        for _ in range(len(min_heap)):
            res.insert(0, heapq.heappop(min_heap)[1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followerMap:
            self.followerMap[followerId].discard(followeeId)
