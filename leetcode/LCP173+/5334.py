# -*- coding: utf-8 -*-
# ======================================
# @File    : 5334.py
# @Time    : 2020/2/9 10:37
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

from collections import defaultdict
class TweetCounts:
    """
    [1348. 推文计数](https://leetcode-cn.com/problems/tweet-counts-per-frequency/)
    """
    def __init__(self):
        self.rec = defaultdict(list)
        self.xd = {
            'minute': 60,
            'hour': 60*60,
            'day': 60*60*24
        }

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.rec[tweetName].append(time)

    @timeit
    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        arr = self.rec[tweetName]
        tic = self.xd[freq]
        res = [0] * ((endTime-startTime) // tic + 1)
        for t in arr:
            if startTime <= t <= endTime:
                res[(t - startTime) // tic] += 1
        return res

if __name__ == '__main__':
    obj = TweetCounts()
    obj.recordTweet('tweet3',0)
    obj.recordTweet('tweet3',60)
    obj.recordTweet('tweet3',10)
    param_2 = obj.getTweetCountsPerFrequency('minute', 'tweet3', 0, 59)
    param_2 = obj.getTweetCountsPerFrequency('minute', 'tweet3', 0, 60)
    obj.recordTweet('tweet3',120)
    param_2 = obj.getTweetCountsPerFrequency('hour', 'tweet3', 0, 210)
    obj.getTweetCountsPerFrequency('hour', 'tweet3', 130, 210)
