import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)   # userId -> [(time, tweetId)]
        self.following = defaultdict(set) # userId -> set of followees

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        users = set(self.following[userId])
        users.add(userId)

        for uid in users:
            for time, tweetId in self.tweets[uid]:
                heapq.heappush(heap, (-time, tweetId))

        res = []
        for _ in range(10):
            if heap:
                res.append(heapq.heappop(heap)[1])
            else:
                break

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        #if followerId != followeeId:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)