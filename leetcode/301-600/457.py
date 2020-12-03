# -*- coding: utf-8 -*-
# ======================================
# @File    : 457.py
# @Time    : 2020/12/2 1:23 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [457. 环形数组循环](https://leetcode-cn.com/problems/circular-array-loop/)
    """
    @timeit
    def circularArrayLoop(self, nums: List[int]) -> bool:
        getnext = lambda i: (n + i + nums[i]) % n
        n = len(nums)
        for i in range(n):
            cur = nums[i]
            # 访问过之后置0
            if cur == 0: continue
            slow, fast = i, getnext(i)
            # 相同方向相乘>0，同时保证fast的两步都是同向
            while cur * nums[fast] > 0 and cur * nums[getnext(fast)] > 0:
                if slow == fast:
                    # 如果相遇，还要判断是否步长为1，让slow再走一步看看是不是自己
                    if slow == getnext(slow):
                        break
                    return True
                slow = getnext(slow)
                fast = getnext(getnext(fast))
            # 将本次路过的节点标记
            slow = i
            while cur * nums[slow] > 0:
                slow, nums[slow] = getnext(slow), 0
        return False


if __name__ == '__main__':
    a = Solution()
    a.circularArrayLoop([2,-1,1,2,2])
    a.circularArrayLoop([-1,2])
    a.circularArrayLoop([-2,1,-1,-2,-2])
    a.circularArrayLoop([1,1,2])
    a.circularArrayLoop([1,2,2,-1])
    a.circularArrayLoop([-1,2,1,2])