# -*- coding: utf-8 -*-
# ======================================
# @File    : 784.py
# @Time    : 2019/11/16 15:39
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [784. 字母大小写全排列](https://leetcode-cn.com/problems/letter-case-permutation/)
    """
    @timeit
    def letterCasePermutation(self, S: str) -> List[str]:
        """
        思路：全排列问题，分别把每个位置的字母大小写转换再回溯就可
        tips：大小写互转的二进制操作是异或32
        """
        # 正向思维
        def dfs(i, cur):
            nonlocal res
            if i == len(S):
                res.append(cur)
                return
            if S[i].isalpha(): dfs(i+1, cur + chr(ord(S[i]) ^ 32))
            dfs(i+1, cur + S[i])
        res = []
        dfs(0, "")
        return res


    @timeit
    def letterCasePermutation2(self, S: str) -> List[str]:
        # 逆向思维
        def dfs(i):
            if i == len(S): return ['']
            res = []
            for x in dfs(i+1):
                if S[i].isalpha():
                    y = chr(ord(S[i]) ^ 32)
                    res += [y + x]
                res += [S[i] + x]
            return res
        return dfs(0)


if __name__ == '__main__':
    a = Solution()
    a.letterCasePermutation("a1b2")
    a.letterCasePermutation2("a1b2")