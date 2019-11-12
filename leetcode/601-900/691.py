# -*- coding: utf-8 -*-
# ======================================
# @File    : 691.py
# @Time    : 2019/11/12 10:59
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
from collections import Counter

class Solution:
    """
    [691. 贴纸拼词](https://leetcode-cn.com/problems/stickers-to-spell-word/)
    """
    @timeit
    def minStickers(self, stickers: List[str], target: str) -> int:
        """
        思路；把target的字母统计出来，再到每个贴纸去计算对target的命中数，按命中数排序
        """
        count_target = Counter(target)
        target = ''.join(sorted([c for c in target]))
        n = len(stickers)
        ds = []
        for i in range(n):
            tmp = Counter(stickers[i])
            ds.append({})
            for k, v in count_target.items():
                if k in tmp:
                    ds[-1][k] = min(v, tmp[k])
        dp = {"": 0}
        def dfs(s):
            if s in dp: return dp[s]
            res = float('inf')
            ctr = Counter(s)
            for d in ds:
                # 每次从贴纸中选字母，把剩余的字母按字典序拼好去递归
                ns = ""
                # 剪枝，对于当前的单词s，如果本次只访问s[0]的话，后面的每个单独字母一定会在后面的递归中作为首字母访问到的
                if not s[0] in d: continue
                for c in ctr:
                    if not c in d:
                        ns += c * ctr[c]
                    else:
                        if ctr[c] > d[c]:
                            ns += c * (ctr[c] - d[c])
                # 剪枝（慢）
                # if ns == s: continue
                print(ns)
                tmp = dfs(ns)
                if tmp < 0: continue
                res = min(res, tmp + 1)
            dp[s] = -1 if res == float('inf') else res
            return dp[s]
        dfs(target)
        return dp[target]

    def minStickers2(self, stickers: List[str], target: str) -> int:
        """
        非递归
        """
        def to_str(bi, s):
            r = ""
            i = 0
            while bi >> i:
                if (bi >> i) & 1:
                    r += s[i]
                i += 1
            return r

        def calc(s, i=0):
            if i == len(s): return {}
            d = {}
            d[s[i]] = 1
            for k, v in calc(s, i+1).items():
                d[s[i] + k] = 1
                d[k] = v
            return d

        n = len(stickers)
        target = ''.join(sorted([c for c in target]))
        count_target = Counter(target)
        ss = []
        for i in range(n):
            tmp = Counter(stickers[i])
            ss.append("")
            for k, v in count_target.items():
                if k in tmp:
                    ss[-1] += k * min(v, tmp[k])
        print(ss)
        ds = []
        for s in ss:
            ds.append(calc(s))
        print(ds)
        nt = len(target)
        boundary = 1 << nt
        dp = {}
        rec = {"": 0}
        for c in list(set(target)):
            dp[c] = [float('inf')] * (nt + 1)
        for d in ds:
            for k in d:
                dp[k[0]][len(k)] = 1
                rec[k] = 1
        for k, v in dp.items():
            if v[1] == float('inf'): return -1
        # 有k个1
        for k in range(1, nt+1):
            i = (1 << k) - 1
            for q in range(nt):
                while i < boundary:
                    i, j = (i << q) + 1, i
                    while j < boundary:
                        s = to_str(j, target)
                        print(s)
                        # if not s in rec:
                        #     res = float('inf')
                        #     rec[s] = -1 if res == float('inf') else res
                        j <<= 1
                    # 更新dp
                    # for
        print(dp)
        print(rec)


if __name__ == '__main__':
    a = Solution()
    a.minStickers2(["with", "example", "science"], "thehat")
    # a.minStickers(["notice", "possible"], "basicbasic")
    # a.minStickers(["notice", "possible", "with", "example", "science", "accuracy", "price", "risk"], "rmpsleththrellc")