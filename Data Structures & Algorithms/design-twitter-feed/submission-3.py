class Tweet:
    def __init__(self, id, user, time, prevTweet = None):
        self.id = id
        self.user = user
        self.time = time
        self.prevTweet = prevTweet

    def __lt__(self, other):
        return self.time > other.time

class Twitter:

    def __init__(self):
        self.userTofollowers = defaultdict(set)
        self.userToPosts = defaultdict(list)
        self.timer = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timer += 1
        tweet = Tweet(tweetId, userId, self.timer)
        if self.userToPosts[userId]:
            tweet.prevTweet = self.userToPosts[userId][-1]
        self.userToPosts[userId].append(tweet)

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.userTofollowers[userId]
        users.add(userId)

        recentFeeds = []
        for user in users:
            if self.userToPosts[user]:
                recentFeeds.append(self.userToPosts[user][-1])
        
        heapq.heapify(recentFeeds)
        feeds = []
        for i in range(10):
            if not recentFeeds:
                break
            tweet = heapq.heappop(recentFeeds)
            feeds.append(tweet.id)
            if tweet.prevTweet:
                heapq.heappush(recentFeeds, tweet.prevTweet)
        return feeds



    def follow(self, followerId: int, followeeId: int) -> None:
        self.userTofollowers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.userTofollowers[followerId].discard(followeeId)
