# -*- coding: utf-8 -*-
# ======================================
# @File    : 470.py
# @Time    : 2019/12/5 13:01
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

# The rand7() API is already defined for you.
# @return a random integer in the range 1 to 7
def rand7(): return __import__('random').randint(1, 7)

class Solution:
    """
    [470. 用 Rand7() 实现 Rand10()](https://leetcode-cn.com/problems/implement-rand10-using-rand7/)
    """
    def rand10(self):
        """
        思路: rand7生成两种数,一种在1~5 (1/5), 另一种确定+5还是+0 (1/2)
        """
        x, y = rand7(), rand7()
        while x > 5: x = rand7()
        while y == 7: y = rand7()
        return x + (y & 1) * 5

    def rand10v2(self):
        # 拒绝采样, 利用两次rand7(),7*7=49种情况, 如果落入[0,40)返回mod(10)后的个位, 否则将9作为其中一个因子再调rand7()
        # 得到9*7=63种情况,再算[1,60]的返回mod(10),否则3*7=21, 当个位只剩下1时,需要重新来过, 也就是调两次rand7()
        a = 1
        x = y = 0
        while True:
            if a == 1:
                a = 7
                x = rand7()
            y = rand7()
            z = (x - 1) * 7 + (y - 1)
            if z < a * 7 - (a * 7) % 10: return (z % 10) + 1
            a = (a * 7) % 10
            x = (z % 10) + 1

if __name__ == '__main__':
    import time
    a = Solution()
    arr = [0] * 10
    t1 = time.time()
    for i in range(100000):
        arr[a.rand10v2() - 1] += 1
    t2 = time.time()
    arr = [e/100000 for e in arr]
    print(arr)
    print(round((t2 - t1), 4))

