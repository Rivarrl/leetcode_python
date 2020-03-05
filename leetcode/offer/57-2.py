# 面试题57 - II. 和为s的连续正数序列
from algorithm_utils import *

class Solution:
    """
    (2a+n-1)n/2 = target
    a = (2t/n-n+1)/2
    枚举n，求a
    """
    @timeit
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res = []
        for n in range(2, target+1):
            a = ((2*target)/n - n + 1) / 2
            x = int(a)
            if x <= 0: break
            if x == a:
                res = [[x+i for i in range(n)]] + res
        return res



if __name__ == '__main__':
    a = Solution()
    a.findContinuousSequence(9)
    a.findContinuousSequence(15)