# -*- coding: utf-8 -*-
# ======================================
# @File    : 1409.py
# @Time    : 2020/4/20 20:54
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1409. 查询带键的排列](https://leetcode-cn.com/problems/queries-on-a-permutation-with-key/)
    """
    @timeit
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        arr = [i for i in range(1, m+1)]
        res = []
        for q in queries:
            i = arr.index(q)
            arr = [q] + arr[:i] + arr[i+1:]
            res.append(i)
        return res

    @timeit
    def processQueries2(self, queries: List[int], m: int) -> List[int]:
        # 树状数组
        # 先把所有m个数放到数组最后占位1，按n=len(queries)次操作，将该位置0，前面空位n-i置1
        n = len(queries)
        nn = n + m + 1
        arr = [0] * (nn)
        lowbit = lambda x: x & (-x)
        def get_sum(i):
            res = 0
            while i > 0:
                res += arr[i]
                i -= lowbit(i)
            return res
        def update(i, val):
            while i < nn:
                arr[i] += val
                i += lowbit(i)
        di = [0] * (m + 1)
        # 占位，放到n+1~n+m+1
        for i in range(1,m+1):
            di[i] = n+i
            update(n+i, 1)
        res = [0] * n
        for i in range(n):
            j = di[queries[i]]
            # 求得索引要-1
            res[i] = get_sum(j) - 1
            # 1-1=0
            update(j, -1)
            # 从n开始向前更新
            di[queries[i]] = n - i
            update(n-i, 1)
        return res


if __name__ == '__main__':
    a = Solution()
    a.processQueries(queries = [3,1,2,1], m = 5)
    a.processQueries(queries = [4,1,2,2], m = 4)
    a.processQueries(queries = [7,5,5,8,3], m = 8)