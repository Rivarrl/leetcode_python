# -*- coding: utf-8 -*-
# ======================================
# @File    : 5.py
# @Time    : 2020/2/10 16:47
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [100267. 理琥珀珠](https://leetcode-cn.com/contest/sf-2020/problems/collect-beads/)
    # 复现官方题解的思路：
    # 1、反复横跳收集珠子
    # 规定先向左跳再向右跳，直至跳到边界时结束这一步
    # 2、即将跳出边界
    # 将其放置，去收集剩下的玻璃珠
    # 3、整理剩下的时候需要挑准起始点，要求最后落到靠内侧的边界处，这样可以刚好将琥珀珠所在的管道倒入，游戏结束。
    # 3.1 如果剩余奇数个，则挑正中间的作为开始，
    # 如果琥珀珠位置在左，就先向右移动
    # 如果琥珀珠位置在右，就先向左移动
    # 3.2 如果剩余偶数个，则按琥珀珠位置决定挑选起始位
    # 如果琥珀珠位置在左，选择中位偏右的作为起始，向左跳
    # 如果琥珀珠位置在右，选择中位偏左的作为起始，向右跳
    # 4、将琥珀珠管道注入非琥珀珠管道
    """
    @timeit
    def collectBeads(self, n: int, amberIndex: int) -> List[List[int]]:
        # 左右跳的边界值
        left = right = a = amberIndex
        # 现象左跳
        direction = -1
        # 跳跃步长，+1
        stride = 1
        # 记录操作
        op = []
        while 0 < a < n-1:
            # 0表示左
            op.append([a, max(0, direction)])
            left = min(left, a)
            right = max(right, a)
            a += stride * direction
            direction *= -1
            stride += 1
        if left == 0 and right == n - 1:
            return op
        def other_collect(lo, hi):
            # lo == 0 说明琥珀在右侧
            _right = lo == 0
            if _right:
                dest = hi
            else:
                dest = lo
            _op = []
            rest = hi - lo + 1
            st = 1
            if rest & 1:
                d = -1 if _right else 1
                a = lo + (hi - lo) // 2
                while a != dest:
                    _op.append([a, max(0, d)])
                    a += st * d
                    d *= -1
                    st += 1
            else:
                d = 1 if _right else -1
                pl = 0 if _right else 1
                a = lo + (hi - lo) // 2 + pl
                while a != dest:
                    _op.append([a, max(0, d)])
                    a += st * d
                    d *= -1
                    st += 1
            return _op

        if a == 0:
            op.extend(other_collect(right+1, n-1))
            op.append([a, 1])
        else:
            op.extend(other_collect(0, left-1))
            op.append([a, 0])
        return op


if __name__ == '__main__':
    a = Solution()
    a.collectBeads(4, 0)