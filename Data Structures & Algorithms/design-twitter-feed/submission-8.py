import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId):
        heap = []
        res = []

        users = self.following[userId]
        users.add(userId)

        # push ONLY latest tweet of each user
        for uid in users:
            tweets = self.tweets[uid]
            if tweets:
                idx = len(tweets) - 1
                time, tid = tweets[idx]
                heapq.heappush(heap, (-time, tid, uid, idx))

        while heap and len(res) < 10:
            neg_time, tid, uid, idx = heapq.heappop(heap)
            res.append(tid)

            # push next older tweet from same user
            if idx > 0:
                idx -= 1
                time, tid = self.tweets[uid][idx]
                heapq.heappush(heap, (-time, tid, uid, idx))

        return res

    def follow(self, followerId, followeeId):
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.following[followerId].discard(followeeId)