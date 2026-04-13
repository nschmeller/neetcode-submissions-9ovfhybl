from collections import defaultdict
from heapq import heappush, heappop

class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.posts = defaultdict(list)
        self.counter = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.counter, tweetId))
        self.counter -= 1


    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        if self.posts[userId] and userId not in self.follows[userId]:
            heappush(heap, (self.posts[userId][len(self.posts[userId])-1], userId, len(self.posts[userId])-1))
        for followee in self.follows[userId]:
            if self.posts[followee]:
                heappush(heap, (self.posts[followee][len(self.posts[followee])-1], followee, len(self.posts[followee])-1))

        res = []
        while len(res) < 10 and heap:
            (tick, tweet), user, idx = heappop(heap)
            res.append(tweet)
            if idx - 1 >= 0:
                heappush(heap, (self.posts[user][idx-1], user, idx-1))
            print(res, heap)

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
