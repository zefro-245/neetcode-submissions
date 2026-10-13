class Twitter:

    def __init__(self):
        self.time = 0
        self.tweet = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweet[userId].append([self.time, tweetId, userId]) 

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []

        # Add the newest tweet of the user themselves
        if self.tweet[userId]:
            i = len(self.tweet[userId]) - 1
            t = self.tweet[userId][i]
            heapq.heappush(maxHeap, [-t[0], t[1], t[2], i])

        # Add the newest tweet of everyone they follow
        for followeeId in self.following[userId]:
            if self.tweet[followeeId]:
                i = len(self.tweet[followeeId]) - 1
                t = self.tweet[followeeId][i]
                heapq.heappush(maxHeap, [-t[0], t[1], t[2], i])

        # Get at most 10 newest tweets
        while maxHeap and len(res) < 10:
            _, tweetId, userId, i = heapq.heappop(maxHeap)
            res.append(tweetId)

            # Add the next newest tweet from the same user
            if i > 0:
                t = self.tweet[userId][i - 1]
                heapq.heappush(maxHeap, [-t[0], t[1], t[2], i - 1])

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
