# -*- coding: utf-8 -*-
# ======================================
# @File    : 355.py
# @Time    : 2020/4/13 1:03
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

from collections import defaultdict

def user():
    return set(), []
class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = defaultdict(user)
        self.tweet_time = defaultdict(int)
        self.ctr = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.users[userId][1].append(tweetId)
        self.ctr += 1
        self.tweet_time[tweetId] = self.ctr

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if not userId in self.users: return []
        res = self.users[userId][1][-10:][::-1]
        for followeeId in self.users[userId][0]:
            if followeeId in self.users:
                cur = self.users[followeeId][1][-10:][::-1]
                i = j = 0
                m, n = len(res), len(cur)
                tmp = []
                while i < m and j < n:
                    if self.tweet_time[res[i]] > self.tweet_time[cur[j]]:
                        tmp.append(res[i])
                        i += 1
                    else:
                        tmp.append(cur[j])
                        j += 1
                if len(tmp) < 10:
                    tmp.extend(res[i:])
                    tmp.extend(cur[j:])
                res = tmp[:10]
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId != followerId:
            self.users[followerId][0].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId != followerId:
            self.users[followerId][0].discard(followeeId)


if __name__ == '__main__':
    twitter = Twitter()
    twitter.postTweet(1, 5)
    twitter.getNewsFeed(1)
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    twitter.getNewsFeed(1)
    twitter.unfollow(1, 2)
    twitter.getNewsFeed(1)