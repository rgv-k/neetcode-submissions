class Twitter:

    def __init__(self):
        self.users_following = defaultdict(set)
        self.users_posts = defaultdict(list)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.users_posts[userId].append((self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.users_following[userId] | {userId}
        heap = []


        for uid in users:
            posts = self.users_posts[uid]
            if posts:
                index = len(posts) - 1
                timestamp, tweetId = posts[index]
                heapq.heappush(
                    heap, (-timestamp, tweetId, uid, index)
                )

        result = []


        while heap and len(result) < 10:
            _, tweetId, uid, index = heapq.heappop(heap)
            result.append(tweetId)


            index -= 1
            if index >= 0:
                timestamp, nextTweetId = self.users_posts[uid][index]
                heapq.heappush(
                    heap, (-timestamp, nextTweetId, uid, index)
                )

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.users_following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users_following[followerId].discard(followeeId)
