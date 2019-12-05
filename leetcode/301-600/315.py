# -*- coding: utf-8 -*-
# ======================================
# @File    : 315.py
# @Time    : 2019/12/5 15:09
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def countSmaller(self, nums: List[int]) -> List[int]:
        # 归并排序，边归并边找逆序数对
        def merge(lo, hi):
            if lo >= hi: return
            mid = lo + (hi - lo) // 2
            merge(lo, mid)
            merge(mid+1, hi)
            left, right = lo, mid+1
            i = lo
            while left <= mid or right <= hi:
                if left > mid:
                    aux[i] = arr[right]
                    oid = arr[right][0]
                    cid = right
                    right += 1
                elif right > hi:
                    aux[i] = arr[left]
                    oid = arr[left][0]
                    cid = left
                    left += 1
                elif arr[left][1] > arr[right][1]:
                    aux[i] = arr[right]
                    oid = arr[right][0]
                    cid = right
                    right += 1
                else:
                    aux[i] = arr[left]
                    oid = arr[left][0]
                    cid = left
                    left += 1
                res[oid] += max(0, i - cid)
                i += 1
            for i in range(lo, hi+1):
                arr[i] = aux[i]

        arr = []
        n = len(nums)
        res = [0] * n
        for idx, num in enumerate(nums):
            arr.append((idx, num))
        aux = [tuple() for _ in range(n)]
        merge(0, n-1)
        return res

    def countSmaller2(self, nums):
        # 倒序向前二分查找 + 按序插入
        import bisect
        q = []
        res = []
        for e in nums[::-1]:
            i = bisect.bisect_left(q, e)
            res.append(i)
            bisect.insort(q, e)
        return res[::-1]



if __name__ == '__main__':
    a = Solution()
    a.countSmaller([5,2,6,1])
