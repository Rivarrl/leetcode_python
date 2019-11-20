# -*- coding: utf-8 -*-
# ======================================
# @File    : 1130.py
# @Time    : 2019/11/20 10:23
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
from functools import lru_cache

class Solution:
    """
    [1130. 叶值的最小代价生成树](https://leetcode-cn.com/problems/minimum-cost-tree-from-leaf-values/)
    """
    @timeit
    def mctFromLeafValues(self, arr: List[int]) -> int:
        """
        思路：动态规划
        对于每个叶节点，arr内部不同的切分可产生不同的二叉树，考虑用dp[i][j]代表arr[i:j+1]的最小代价。
        i=j时一定是0，因为arr[i:j+1]只有一个值，是叶节点。
        比如[6,2,4]，dp[0][2] = min(dp[0][0] + dp[1][2] + max(arr[0:1]) * max(arr[1:3]), dp[0][1] + dp[2][2] + max(arr[0:2]) * max(arr[2:3]))
        = min(0 + 8 + 6*4, 12 + 0 + 6 * 4) = 32
        时间复杂度：O(n^3)
        """
        n = len(arr)
        dp = [[-1] * n for _ in range(n)]
        mx = [[0] * n for _ in range(n)]
        for width in range(n):
            for left in range(n - width):
                right = left + width
                if left == right:
                    mx[left][right] = arr[left]
                else:
                    mx[left][right] = max(mx[left][right-1], mx[left+1][right])
        @lru_cache(None)
        def dfs(i, j):
            if i == j: return 0
            if i == j - 1: return arr[i] * arr[j]
            if dp[i][j] != -1: return dp[i][j]
            res = 1 << 31
            for k in range(i, j):
                res = min(res, dfs(i, k) + dfs(k+1, j) + mx[i][k] * mx[k+1][j])
            dp[i][j] = res
            return res
        return dfs(0, n-1)


    @timeit
    def mctFromLeafValues2(self, arr: List[int]) -> int:
        """
        思路：单调栈
        有一种贪心的思想，我们总代价最小就是让那个较大的数较早的结束运算，换句话说就是让较大的数所在的树枝深度尽可能小。
        比如[6,2,4]，总代价最小就是让6做最少次数的乘法，也就是放到二叉树较矮的一边，也就是左边[6|2,4]，
        如果三个数中较大的值在中间，比如[2,6,4]，较大的值不可避免的要做两次乘法，这种情况需要让次大的值尽可能少的做乘法。
        所以把4放到二叉树较矮的一边，也就是右边[2,6|4]。
        上面两种情况，我们可以发现一个规律，由题意，数字2（三个数中最小的那个）无论在何种排列中，它都会在较长的一边（只做一次计算就废弃掉）
        用一个单调递减的栈可以实现上述功能：
        case 1: 6，2入栈，4的加入破坏了单调性，于是需要比较6和4，取较小的一个，和2做乘法再把2弹出，4入栈
        case 2: 2入栈，6的加入破坏了单调性，2弹出后就栈空了，所以只能和6做乘法，6入栈
        一般情况：[6,4,3,2,5]，6,4,3,2入栈，5加入会造成弹出2，3，4
        这时候需要每弹出一个数做一次乘法（较小的值2*min(栈顶元素, 5)），弹出较小的
        时间复杂度：O(n)
        """
        stk = []
        res = 0
        for x in arr:
            while stk and stk[-1] < x:
                s1 = stk.pop()
                s2 = x if not stk else min(x, stk[-1])
                res += s1 * s2
            stk.append(x)
        if stk:
            res += sum([stk[i] * stk[i-1] for i in range(1, len(stk))])
        return res


if __name__ == '__main__':
    a = Solution()
    a.mctFromLeafValues([6,2,4])
    a.mctFromLeafValues2([6,2,4])